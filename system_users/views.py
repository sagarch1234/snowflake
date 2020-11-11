from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import  RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from system_users.models import User, EmailVerificationOtp, InvitedMembers, CompanyDetails, InvitedSuperUsers
from system_users.serializers import (
    RegisterUpdateUserSerializer, RetriveUserProfileSerializer, ChangePasswordSerializer,
    TokenObtainPairSerializer, InvitedMemberSerializer, RegisterInvitedUserSerializer,
    CompanyDetailsSerializer, ResendVerificationMailSerializer, RegisterSuperAdminSerializer,
    InvitedSuperUserSerializer)
from system_users.utilities import store_otp, generate_otp, verify_otp_exist
from system_users.tasks import send_forgot_password_otp_mail, send_email_verification_mail
from system_users.permissions import IsInviteOwner, WhitelistOrganisationAdmin, IsCompanyOwner, WhitelistSuperAdmin
from system_users.constants import ORGANISATION_MEMBER, SUPER_ADMIN, ORGANISATION_ADMIN

from django.db import transaction, IntegrityError
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.hashers import check_password
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_simplejwt.views import TokenObtainPairView

from snowflake_optimizer.settings import SECRET_KEY

import jwt, time


class RegisterInvitedMember(APIView):
    '''
    This view is to onboard invited users.

    sample JSON -

    {
        "first_name": "Sagar",
        "last_name": "Patel",
        "mobile_number": 9765136448, #optional
        "password": "123456"
    }

    This view also need a query parameter 'token' to onboard the invited user.
    The invited member will be onboarded as Organisation Member. 
    This view is only for Organisation Admin. 
    '''
    

    def post(self, request, format=None):
        '''
        '''
        #check if the provided token is valid.
        try:
                
            decoded_jwt = jwt.decode(request.query_params['token'], SECRET_KEY, algorithms=['HS256'])

        except ExpiredSignatureError as expired:
                
            return Response({
                "error" : "Invite has expired",
                "status" : status.HTTP_406_NOT_ACCEPTABLE
            })
            
        except InvalidSignatureError as invalid:

            return Response({
                "error" : "Invite token Invalid.",
                "status" : status.HTTP_406_NOT_ACCEPTABLE
            })

        #cross check if user is invited or not.
        try:
            
            invited_member_obj = InvitedMembers.objects.get(email=decoded_jwt['email'])

        except InvitedMembers.DoesNotExist:
            
            return Response({
                "error" : "Invite not found.",
                "status" : status.HTTP_400_BAD_REQUEST
            })

        # check if the invited member is onboarded or not.
        if invited_member_obj.is_onboarded == True:

            return Response({
                "error" : "You account has already been created.",
                "status" : status.HTTP_400_BAD_REQUEST
            })

        serialized_data = RegisterInvitedUserSerializer(data=request.data)

        if serialized_data.is_valid():

            serialized_data.validated_data['is_mobile_number_verified'] = False
            serialized_data.validated_data['is_email_varified'] = True
            # this will active user account and allow user to login.
            serialized_data.validated_data['is_active'] = True
            #this will make user join the same company through which the invitation was sent to the user.
            serialized_data.validated_data['company'] = decoded_jwt['company_name']
            serialized_data.validated_data['email'] = decoded_jwt['email']
            #this will make user join as an Organisation Member.
            serialized_data.validated_data['user_group'] = ORGANISATION_MEMBER

            try:
            
                user = serialized_data.save()
            
            except IntegrityError as error:

                return Response ({
                    "error": str(error),
                    "status": status.HTTP_226_IM_USED
                    })
        
        else:
        
            return Response(serialized_data.errors)

        if user == None:

            return Response({
                "message" : "Oppsss.. something went wrong.",
                "status" : status.HTTP_409_CONFLICT
            })

        else:

            return Response({
                "message":"Your account has been created and activated." ,
                "status":status.HTTP_200_OK
            })


class TokenObtainPairView(TokenObtainPairView):
    '''
    This is to over ride the default serializer provided to TokenObtainPairView from simple JWT.
    To add extra key and value ('group' = group_name) to the login response we had to create and inherite the serializer class TokenObtainPairSerializer.
    '''
    serializer_class = TokenObtainPairSerializer


class RegisterUserView(APIView):

    '''
    This view is to register a new user.

    API request body -
    
    {
        "first_name": "Jeet",
        "last_name": "Patel",
        "mobile_number": 9765136677, #optional
        "email": "jpatel9996@gmail.com",
        "password": "123456",
        "company": {
            "company_name": "Hello Inc"
        }
    }
    This view does not require authentication.
    This view will register user as an Organisation Admin.
    '''

    def post(self, request, format=None):

        '''
        '''
        serialized_data = RegisterUpdateUserSerializer(data=request.data)

        if serialized_data.is_valid():

            serialized_data.validated_data['is_mobile_number_verified'] = False
            #user will have to verify email.
            serialized_data.validated_data['is_email_varified'] = False
            #user wont be able to login as email has not been verified.
            serialized_data.validated_data['is_active'] = False
            #register user as an organisation Member
            serialized_data.validated_data['user_group'] = ORGANISATION_ADMIN

            try:
            
                user = serialized_data.save()
            
            except IntegrityError as error:

                return Response ({
                    "error": str(error),
                    "status": status.HTTP_226_IM_USED
                    })
            
        
        else:
        
            return Response(serialized_data.errors)

        if user == None:

            return Response({
                "message" : "Oppsss.. something went wrong.",
                "status" : status.HTTP_409_CONFLICT
            })

        else:

            return Response({
                "message":"Verification mail has been sent to your email '" + request.data['email'] +  "'. Please provide the OTP to verify your email and active your account. " ,
                "status":status.HTTP_200_OK
            })


class RetriveUserProfileView(RetrieveAPIView):
    
    '''
    This view will retrive user profile information for the authenticated user and for the SUPER ADMIN type of user.
    
    Case : 1
        1. If you want to retrive some othe user's profile then login using SUPER ADMIN's credentials and then provide  ```**'organisation_admin_id'**``` as
           query paramter to the end point along with the valid access token.
        
        2. ```request body``` will be ignored in this case even if provided.
        
        3. ```query_parameters``` as ```**'organisation_admin_id'**``` is required. If any other parameter is provided then those parameter will be ignored.

    Case : 2
        1. If you want to retrive the profile of the authenticated user then just send the request to the endpoint with valid the valid access token. 

        2. In this case ```request body``` and ```query_parameter``` will be ignored even if provided.

    Sample response -

    {
        "first_name": "Jeet",
        "last_name": "Patel",
        "email": "jpatel9996@gmail.com",
        "mobile_number": 9765136677,
        "company_name": "Hello Inc",
        "user_group": [
            {
                "id" : 1,
                "name" : "Organisation Admin" 
            }
        ]
    }
    '''

    permission_classes = [IsAuthenticated | (WhitelistSuperAdmin)]

    def get_object(self):

        current_user_group = list(self.request.user.groups.values('name'))

        # if str(Group.objects.get(name=SUPER_ADMIN)) == current_user_group[0]['name']:

        #     return User.objects.get(pk=self.request.query_params['organisation_admin_id'])

        return User.objects.get(pk=self.request.user.id)

    def retrieve(self, request):

        queryset = self.get_object()
        serializer_class = RetriveUserProfileSerializer
        serialized_data = serializer_class(queryset)
        return Response(serialized_data.data)


class ActivateAccountView(APIView):

    '''
    Before login into the paltform after registeration user will have to activate his/her account by verifying the registered email address.

    {{host}}/api/users/activate-account/?email=&otp=
    '''

    def put(self, request, format=None):

        '''
        This method will take email and otp in the query parameters as shown below.

        {{host/url}}/users/activate-account/?email=jpatel99967@gmail.com&otp=8898
        
        If the otp of the provided email is same as the otp stored in the database for the provided email then the account will be activated and user will be able to login.
        This is a mandtory step after registering as an organisation admins to active account.
        This view doesn't require authentication.
        '''
        #check if user exist in database.
        try:
            
            user = User.objects.get(email=request.query_params['email'])

        except User.DoesNotExist:
            
            return Response({
                "error" : "User with email '" + request.query_params['email'] + "' does not exist.",
                "status" : status.HTTP_404_NOT_FOUND
            })
        # check if otp has been generated and get the generated otp.
        try:
            
            otp_instance = EmailVerificationOtp.objects.get(user=user)

        except EmailVerificationOtp.DoesNotExist:
            
            return Response({
                "error" : "Email verification request was never raised for '" + request.query_params['email'] + "'.",
                "status" : status.HTTP_400_BAD_REQUEST
            })
        # compare the provided otp and the otp in database.
        if request.query_params['otp'] == str(otp_instance.otp):
            #delete otp if it exist.
            otp_instance.delete()
            #active user account.
            user.is_active = True
            #mark user email as verified.
            user.is_email_varified = True
            #update user instance in database.
            user.save(update_fields=['is_active', 'is_email_varified'])            

            return Response({
                "message" : "Your account has been activated.",
                "status" : status.HTTP_200_OK
            })

        return Response({
            "error":"Incorrect OTP.",
            "status":status.HTTP_400_BAD_REQUEST
        })

            
class ChangePasswordView(APIView):

    '''
    This view will help user change their current password.

    Authentication is required for this view.

    Sample JSON -
    {
        "change_password":"",
        "new_password":""
    }
    '''

    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):

        '''
        '''
        # check user existance and get the user instance.
        user_instance = get_object_or_404(User, pk=request.user.id)
        
        serialized_data = ChangePasswordSerializer(user_instance, data=request.data)

        if serialized_data.is_valid():
            #compare password of user in database with the current_password received in request.data .
            if not check_password(request.data['current_password'], user_instance.password):

                return Response({
                    "error" : "Current password is not correct.",
                    "status" : status.HTTP_400_BAD_REQUEST
                })
            
            else:

                user_instance = serialized_data.save()

                return Response({
                    "message" : "Your password has been updated. Please use your new password to login.",
                    "status" : status.HTTP_200_OK
                })

        else:
            return Response(serialized_data.errors)


class UpdateProfileView(APIView):

    '''
    This view will updated user profile information.

    The following profile information can be updated.
    
    {
        "first_name": "Jeet",
        "last_name": "Patel",
        "mobile_number": 97651367798,
        "email": "jpatel99967@gmail.com",
    }

    Not all the above mentioned key values are required every time. Only send the key values which needs to be updated. (Partial updates works fine for this view.)
    '''

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return User.objects.get(pk=self.request.user.id)

    def put(self, request, format=None):
        #get the query set
        queryset = self.get_queryset()
        serialized_data = RegisterUpdateUserSerializer(queryset, data=request.data, partial=True)

        if serialized_data.is_valid():

            try:
        
                updated_instance = serialized_data.save()

                return Response({
                    "message" : "Profile details updated.",
                    "status" : status.HTTP_200_OK
                })
            
            except IntegrityError as error:
            
                return Response({
                    "error":str(error),
                    "status": status.HTTP_226_IM_USED
                })
        else:
            
            return Response(serialized_data.errors)
        
        
class InviteMemberView(APIView):
    '''
    Organisation Admin can invite members to join the company profile. The invited member will be onboarded as Organisation Member.
    This view is only for Organisation Admin.

    Sample JSON -
    {
        "email":""
    }
    '''

    permission_classes = [IsAuthenticated & WhitelistOrganisationAdmin]

    def post(self, request, format=None):

        # check if the user with the same email already exist or not.
        
        try:
            
            user_existance = User.objects.get(email=request.data['email'])

        except User.DoesNotExist:

            #generate the encoded jwt if user does not exist.
            
            encoded_jwt = jwt.encode({
                'company_name':request.user.company.company_name,
                'email': request.data['email'],
                'exp' : time.time() + 10080}, SECRET_KEY, algorithm='HS256').decode('utf-8')

            #add the encoded_jwt to the request.data
            request.data['token'] = encoded_jwt

            serialized_data = InvitedMemberSerializer(data=request.data)

            if serialized_data.is_valid():

                #provide the instance of the user who requested to invited a user.
                serialized_data.validated_data['invited_by'] = request.user
                    
                invite_instance = serialized_data.save()

                return Response({
                    "message":"Invite sent.",
                    "status" : status.HTTP_200_OK
                })

            else:

                return Response(serialized_data.errors)

        if not user_existance is None:
            
            return Response({
                "error" : "User already associated with this email address.",
                "status" : status.HTTP_400_BAD_REQUEST
            })
        

class VerifyInviteView(APIView):
    '''
    This view is to verify the invite token generated to onboard Organisation Member and Super Admin.
    It need only one query_parameter - `token`

    {{host}}/api/users/verify-invite/?token=

    No request body is required.
    '''
    def post(self, request, format=None):
        # decode and validated provided jwt token.
        try:
            
            decoded_jwt = jwt.decode(request.query_params['token'], SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError as expired:
            
            return Response({
                "error" : "Invite has expired",
                "status" : status.HTTP_406_NOT_ACCEPTABLE
            })
        
        except jwt.InvalidSignatureError as invalid:
        
            return Response({
                "error" : "Invite token Invalid.",
                "status" : status.HTTP_406_NOT_ACCEPTABLE
            })

        return Response({
            "message" : "Invite Validated.",
            "status" : status.HTTP_202_ACCEPTED
        })


class ResendInviteView(APIView):
    '''
    This view will regenerate token, update it into the InvitedMembers model and resend member invite mail. 

    This view require a `query_params` as `invite_id` and `email` in JSON body as shown below -

    {{host}}/api/users/resend-invite/?invite_id=17
    
    Sample input data -

    {
        "email":""
    }
    '''
    permission_classes = [IsAuthenticated & IsInviteOwner]

    def post(self, request, format=None):
        
        # check if user has already been invited.
        try:
        
            invited_member_obj = InvitedMembers.objects.get(pk=request.query_params['invite_id'])

        except InvitedMembers.DoesNotExist:
            
            return Response({
                "error" : "Invite was never sent to the provided email.",
                "status" : status.HTTP_404_NOT_FOUND
            })
        # check if users is already registered.
        try:
            
            user_existance = User.objects.get(email=request.data['email'])

        except User.DoesNotExist:
            
            encoded_jwt = jwt.encode({
                'company_name':request.user.company.company_name,
                'email': request.data['email'],
                'exp' : time.time() + 10080}, SECRET_KEY, algorithm='HS256').decode('utf-8')

            request.data['token'] = encoded_jwt

            serialized_data = InvitedMemberSerializer(invited_member_obj, data=request.data)

            if serialized_data.is_valid():
                    
                invite_instance = serialized_data.save()

                return Response({
                    "message":"Invite sent again.",
                    "status" : status.HTTP_200_OK
                })

            else:

                return Response(serialized_data.errors)
            
        if not user_existance is None:
            
            return Response({
                "error" : "User already associated with this email address.",
                "status" : status.HTTP_400_BAD_REQUEST
            })


class UpdateCompanyDetaisView(APIView):
    '''
    This view allows Organisation Admin to update the Company Detials. 
    {
        "id":,
        "company_name":""
    } 
    '''
    
    permission_classes = [IsAuthenticated & WhitelistOrganisationAdmin & IsCompanyOwner]

    def get_queryset(self):

        return CompanyDetails.objects.get(pk=self.request.data['id'])

    def put(self, request, format=None):
        #get company instance which has to be updated.
        company_instance  = self.get_queryset()

        serialized_data = CompanyDetailsSerializer(company_instance, data=request.data)

        if serialized_data.is_valid():
            
            updated_instance = serialized_data.save()

            return Response({
                "message":"Company details has been updated.",
                "status":status.HTTP_200_OK
            })
     
        else:
            return Response(serialized_data.errors)


class ListInvitedMembers(ListAPIView):
    '''
    This will list all the email address to which the invite has been sent.
    This will only list the email address to which the requested user has sent the invites.
    It provide the search funcationality on `email`.
    It also has pagination.
    This view returns a list ordered in descending of field `id`.

    {{host}}/api/users/list-invited-members/?is_onboarded=&search=&page=

    `is_onboarded` is a boolean value. If you want to list the onboarded users then pass `is_onboarded=True` or else `is_onboarded=False`

    Access to authenticated users only. 

    If user is of type `SUPER ADMIN` then provide `organisation_admin_id` as a query parameter.

    ```request body``` will be ignored for every type of user.

    ```query_params``` will be ignored if the authenticated user trying to access the view is not of type ```SUPER ADMIN```.
    '''
    
    IsObjectOwner = WhitelistOrganisationAdmin & IsCompanyOwner

    permission_classes = [IsAuthenticated & ( IsObjectOwner | WhitelistSuperAdmin )]
    
    serializer_class = InvitedMemberSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['is_onboarded']
    search_fields = ['email']
    ordering=['-id']
    pagination_class = PageNumberPagination

    def get_queryset(self):

        current_user_group = list(self.request.user.groups.values('name'))

        if str(Group.objects.get(name=SUPER_ADMIN)) == current_user_group[0]['name']:

            return InvitedMembers.objects.filter(invited_by=self.request.query_params['organisation_admin_id'])

        return InvitedMembers.objects.filter(invited_by=self.request.user)


class ListCompanyUsersView(ListAPIView):
    '''
    This view will list all the users belonging to the same company.
    
    It provide the search funcationality on 'first_name', 'last_name' and 'email'.
    
    It also has pagination.

    This view returns a list ordered in descending of id.

    If the authenticated user trying to access the view is of type ```SUPER ADMIN``` then provide the ```query_parameter``` as ```company_id```.

    If the authenticated user trying to access the view is not of type ```SUPER ADMIN``` then provides the ```query_parameter``` as ```company_id``` will be ignored 
    and the API and the list of company members will be returned belongig to the company of authenticated user trying to access the view.

    '''
    permission_classes = [IsAuthenticated & ( WhitelistOrganisationAdmin | WhitelistSuperAdmin )]
    
    serializer_class = RegisterUpdateUserSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering=['-id']
    search_fields = ['first_name', 'last_name', 'email']
    pagination_class = PageNumberPagination

    def get_queryset(self):

        current_user_group = list(self.request.user.groups.values('name'))

        if str(Group.objects.get(name=SUPER_ADMIN)) == current_user_group[0]['name']:

            return User.objects.filter(company=self.request.query_params['company_id'])

        return User.objects.filter(company=self.request.user.company)


class ResendEmailVerificationView(APIView):
    '''
    This view is to resend email verification mail to activate user account.

    Sample request body -
    
    {
        "email":""
    }
    '''
    
    def post(self, request, formate=None):
        
        serialized_data = ResendVerificationMailSerializer(data=request.data)

        if serialized_data.is_valid():
            #check if user exist in the database.
            try:

                user_instance = User.objects.get(email=request.data['email'])
            
            except User.DoesNotExist:
            
                return Response({
                    "error" : "User never registered.",
                    "status" : status.HTTP_200_OK
                })
            #check if user's email is already verified or not.
            if user_instance.is_email_varified == False:
                #check if otp exist.  
                otp_exist = verify_otp_exist(user_instance.id)

                if otp_exist['status'] == status.HTTP_404_NOT_FOUND:
                    #generate and store otp if it does not exist
                    otp = store_otp(otp = generate_otp(), user_instance = user_instance)

                elif otp_exist['status'] == status.HTTP_302_FOUND:

                    otp = otp_exist['otp']
                # send email with the otp.
                send_email_verification_mail.delay(first_name=user_instance.first_name, otp=otp, email=user_instance.email)

                return Response({
                    "message":"verification mail has been sent to '" + user_instance.email + "'.",
                    "status":status.HTTP_200_OK
                })

            elif user_instance.is_email_varified == True:

                return Response({
                    "error" : "User's email already varified.",
                    "status": status.HTTP_200_OK
                })
                

class ListCompaniesView(ListAPIView):
    '''
    This view will list companies registered with this system with their Organistion Admin details.
    This view has the search funcationality which works on `company_name`.
    It also has pagination.
    This view returns a list ordered in descending of id.

    {{host}}/api/users/list-companies/?search=&page=

    '''
    permission_classes = [IsAuthenticated & WhitelistSuperAdmin]

    serializer_class = CompanyDetailsSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering = ['-id']
    search_fields = ['company_name']
    pagination_class = PageNumberPagination

    def get_queryset(self):

        queryset = CompanyDetails.objects.all()

        return queryset


class SuperUserInviteView(APIView):
    '''
    Invite super users to the system.
    The invited member will be onboarded as Super Admin.
    This view is only for Super Admin.

    Sample JSON -
    {
        "email":""
    }
    '''
    
    permission_classes = [IsAuthenticated & WhitelistSuperAdmin]

    def post(self, request, format=None):
        # check if email exist in database.
        try:
            
            user_existance = User.objects.get(email=request.data['email'])

        except User.DoesNotExist:
            #generate encoded jwt
            encoded_jwt = jwt.encode({
                'email': request.data['email'],
                'exp' : time.time() + 10080}, SECRET_KEY, algorithm='HS256').decode('utf-8')

            request.data['token'] = encoded_jwt
            request.data['invited_by'] = request.user.id

            serialized_data = InvitedSuperUserSerializer(data=request.data)

            if serialized_data.is_valid():

                serialized_data.validated_data['invited_by'] = request.user
                    
                invite_instance = serialized_data.save()

                return Response({
                    "message":"Invite sent.",
                    "status" : status.HTTP_200_OK
                })

            else:

                return Response(serialized_data.errors)

        if not user_existance is None:
            
            return Response({
                "error" : "User already associated with this email address.",
                "status" : status.HTTP_400_BAD_REQUEST
            })


class ResendSuperUserInvite(APIView):
    '''
    This view will regenerate token, update it into the InvitedSuperUsers model and resend member invite mail. 

    This view require a `query_params` as `invite_id` and `email` in JSON body as shown below -

    {{host}}/api/users/resend-super-user-invite/?invite_id=17
    
    Sample input data -

    {
        "email":""
    }
    '''

    def post(self, request, format=None):
        # check if user has already been invited.
        try:
        
            invited_member_obj = InvitedSuperUsers.objects.get(pk=request.query_params['invite_id'])

        except InvitedMembers.DoesNotExist:
            
            return Response({
                "error" : "Invite was never sent to the provided email.",
                "status" : status.HTTP_404_NOT_FOUND
            })
        # check if users is already registered.
        try:
            
            user_existance = User.objects.get(email=request.data['email'])

        except User.DoesNotExist:
            #generate encoded jwt.
            encoded_jwt = jwt.encode({
                'email': request.data['email'],
                'exp' : time.time() + 10080}, SECRET_KEY, algorithm='HS256').decode('utf-8')

            request.data['token'] = encoded_jwt

            serialized_data = InvitedSuperUserSerializer(invited_member_obj, data=request.data)

            if serialized_data.is_valid():
                    
                invite_instance = serialized_data.save()

                return Response({
                    "message":"Invite sent again.",
                    "status" : status.HTTP_200_OK
                })

            else:

                return Response(serialized_data.errors)
            
        if not user_existance is None:
            
            return Response({
                "error" : "User already associated with this email address.",
                "status" : status.HTTP_400_BAD_REQUEST
            })


class RegisterSuperAdminView(APIView):
    '''
    This view is to onboard invited users.

    sample JSON -

    {
        "first_name": "Sagar",
        "last_name": "Patel",
        "mobile_number": 9765136448, #optional
        "password": "123456"
    }

    This view also need a query parameter 'token' to onboard the invited user.
    The invited member will be onboarded as Super Member. 
    This view is only for Super Admin.
    '''
    def post(self, request, format=None):
        #decode received jwt
        try:
                
            decoded_jwt = jwt.decode(request.query_params['token'], SECRET_KEY, algorithms=['HS256'])

        except ExpiredSignatureError as expired:
                
            return Response({
                "error" : "Invite has expired",
                "status" : status.HTTP_406_NOT_ACCEPTABLE
            })
            
        except InvalidSignatureError as invalid:

            return Response({
                "error" : "Invite token Invalid.",
                "status" : status.HTTP_406_NOT_ACCEPTABLE
            })
        #verify if email exist in the invite list.
        try:
            
            invited_member_obj = InvitedSuperUsers.objects.get(email=decoded_jwt['email'])

        except InvitedSuperUsers.DoesNotExist:
            
            return Response({
                "error" : "Invite not found.",
                "status" : status.HTTP_400_BAD_REQUEST
            })
        #check if the invited memeber is already onboarded or not.
        if invited_member_obj.is_onboarded == True:

            return Response({
                "error" : "You account has already been created.",
                "status" : status.HTTP_400_BAD_REQUEST
            })

        serialized_data = RegisterSuperAdminSerializer(data=request.data)

        if serialized_data.is_valid():

            serialized_data.validated_data['is_mobile_number_verified'] = False
            #mark email as verified.
            serialized_data.validated_data['is_email_varified'] = True
            #activate user account so that user could login when registered.
            serialized_data.validated_data['is_active'] = True
            
            # serialized_data.validated_data['company'] = decoded_jwt['company_name']
            serialized_data.validated_data['email'] = decoded_jwt['email']
            #onboard user as Super Admin.
            serialized_data.validated_data['user_group'] = SUPER_ADMIN

            try:
            
                user = serialized_data.save()
            
            except IntegrityError as error:

                return Response ({
                    "error": str(error),
                    "status": status.HTTP_226_IM_USED
                    })
            
        else:
        
            return Response(serialized_data.errors)

        if user == None:

            return Response({
                "message" : "Oppsss.. something went wrong.",
                "status" : status.HTTP_409_CONFLICT
            })

        else:

            return Response({
                "message":"Your account has been created and activated." ,
                "status":status.HTTP_200_OK
            })


class ListInvitedSuperAdminView(ListAPIView):
    '''
    This will list all the email address to which the invite has been sent.
    This will only list the email address to which the requested user has sent the invites.
    It provide the search funcationality on 'email'.
    It also has pagination.
    This view returns a list ordered in descending of id.

    {{host}}/api/users/list-invited-super-admins/?is_onboarded=false&email=&page=

    `is_onboarded` is a boolean value. If you want to list the onboarded users then pass `is_onboarded=True` or else `is_onboarded=False`
    '''
    permission_classes = [IsAuthenticated & WhitelistSuperAdmin]
    
    serializer_class = InvitedSuperUserSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['is_onboarded']
    search_fields = ['email']
    ordering=['-id']
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = InvitedSuperUsers.objects.all()
        return queryset
