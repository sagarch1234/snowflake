from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import  RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from system_users.models import User, EmailVerificationOtp, InvitedMembers, CompanyDetails
from system_users.serializers import (
    RegisterUpdateUserSerializer, RetriveUserProfileSerializer, ChangePasswordSerializer,
    TokenObtainPairSerializer, InvitedMemberSerializer, RegisterInvitedUserSerializer,
    CompanyDetailsSerializer, ResendVerificationMailSerializer)
from system_users.utilities import store_otp, generate_otp, verify_otp_exist
from system_users.tasks import send_forgot_password_otp_mail, send_email_verification_mail
from system_users.permissions import IsInviteOwner, WhitelistOrganisationAdmin, IsCompanyOwner
from system_users.constants import ORGANISATION_MEMBER

from django.db import transaction, IntegrityError
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
        "mobile_number": 9765136448,
        "password": "123456"
    }

    This view also need a query parameter 'token' to onboard the invited user.
    '''

    def post(self, request, format=None):
        '''
        '''
        
        try:
            
            invited_member_obj = InvitedMembers.objects.get(token=request.query_params['token'])

        except InvitedMembers.DoesNotExist:
            
            return Response({
                "error" : "Invite not found.",
                "status" : status.HTTP_400_BAD_REQUEST
            })
        
        if invited_member_obj.is_onboarded == True:

            return Response({
                "error" : "You account has already been created.",
                "status" : status.HTTP_400_BAD_REQUEST
            })

        serialized_data = RegisterInvitedUserSerializer(data=request.data)

        if serialized_data.is_valid():

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

            serialized_data.validated_data['is_mobile_number_verified'] = False
            serialized_data.validated_data['is_email_varified'] = True
            serialized_data.validated_data['is_active'] = True
            
            serialized_data.validated_data['company'] = decoded_jwt['company_name']
            serialized_data.validated_data['email'] = decoded_jwt['email']

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
        "mobile_number": 9765136677,
        "email": "jpatel9996@gmail.com",
        "password": "123456",
        "company": {
            "company_name": "Hello Inc"
        }
    }
    '''

    def post(self, request, format=None):

        '''
        '''

        serialized_data = RegisterUpdateUserSerializer(data=request.data)

        if serialized_data.is_valid():

            serialized_data.validated_data['is_mobile_number_verified'] = False
            serialized_data.validated_data['is_email_varified'] = False
            serialized_data.validated_data['is_active'] = False

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
                "message":"Verification mail has been sent to your email '" + request.data['email'] +  "'. Please provide the OTP to verify your email and active your account. " ,
                "status":status.HTTP_200_OK
            })


class RetriveUserProfileView(RetrieveAPIView):
    
    '''
    This view will retrive user profile information.

    Authentication is required for this view.

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
                "name" : "Admin" 
            }
        ]
    }
    '''

    permission_classes = [IsAuthenticated]

    def get_object(self):

        return User.objects.get(pk=self.request.user.id)

    def retrieve(self, request):

        queryset = self.get_object()
        serializer_class = RetriveUserProfileSerializer
        serialized_data = serializer_class(queryset)
        return Response(serialized_data.data)


class ActivateAccountView(APIView):

    '''
    Before login into the paltform after registeration user will have to activate his/her account by verifying the registered email address.
    '''

    def put(self, request, format=None):

        '''
        This method will take email and otp in the query parameters as shown below.

        {{host/url}}/users/activate-account/?email=jpatel99967@gmail.com&otp=8898
        
        If the otp of the provided email is same as the otp stored in the database for the provided email then the account will be activated and user will be able to login again.
        '''

        try:
            
            user = User.objects.get(email=request.query_params['email'])

        except User.DoesNotExist:
            
            return Response({
                "error" : "User with email '" + request.query_params['email'] + "' does not exist.",
                "status" : status.HTTP_404_NOT_FOUND
            })
        
        try:
            
            otp_instance = EmailVerificationOtp.objects.get(user=user)

        except EmailVerificationOtp.DoesNotExist:
            
            return Response({
                "error" : "Email verification request was never raised for '" + request.query_params['email'] + "'.",
                "status" : status.HTTP_400_BAD_REQUEST
            })
        
        if request.query_params['otp'] == str(otp_instance.otp):

            otp_instance.delete()

            user.is_active = True
            user.is_email_varified = True

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
    '''

    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):

        '''
        '''
        user_instance = get_object_or_404(User, pk=request.user.id)
        
        serialized_data = ChangePasswordSerializer(user_instance, data=request.data)

        if serialized_data.is_valid():

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
    '''

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        '''
        '''

        return User.objects.get(pk=self.request.user.id)

    def put(self, request, format=None):
        '''
        '''

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
    '''
    permission_classes = [IsAuthenticated & WhitelistOrganisationAdmin]

    def post(self, request, format=None):
        '''
        '''
        try:
            
            user_existance = User.objects.get(email=request.data['email'])

        except User.DoesNotExist:
            
            encoded_jwt = jwt.encode({
                'company_name':request.user.company.company_name,
                'email': request.data['email'],
                'exp' : time.time() + 10080}, SECRET_KEY, algorithm='HS256').decode('utf-8')

            request.data['token'] = encoded_jwt

            serialized_data = InvitedMemberSerializer(data=request.data)

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
        

class VerifyInviteView(APIView):
    '''
    This view is to verify the invite token.
    It need only one query_parameter - `token`
    No request body is required.
    '''
    def post(self, request, format=None):
        '''
        '''
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

        return Response({
            "message" : "Invite Validated.",
            "status" : status.HTTP_202_ACCEPTED
        })


class ResendInviteView(APIView):
    '''
    This view will regenerate token, update it into the InvitedMembers model and resend member invite mail. 

    This view require a query_params as invite_id.
    '''
    permission_classes = [IsAuthenticated & IsInviteOwner]

    def post(self, request, format=None):
        '''
        '''
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
                print(invite_instance)

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
    '''
    
    permission_classes = [IsAuthenticated & WhitelistOrganisationAdmin & IsCompanyOwner]

    def get_queryset(self):

        return CompanyDetails.objects.get(pk=self.request.data['id'])

    def put(self, request, format=None):
        '''
        '''
        
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
    '''
    permission_classes = [IsAuthenticated & WhitelistOrganisationAdmin & IsCompanyOwner]
    
    serializer_class = InvitedMemberSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['is_onboarded']
    search_fields = ['email']
    ordering=['-id']
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = InvitedMembers.objects.filter(invited_by=self.request.user)
        return queryset


class ListCompanyUsersView(ListAPIView):
    '''
    '''
    permission_classes = [IsAuthenticated & WhitelistOrganisationAdmin]
    
    serializer_class = RegisterUpdateUserSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering=['-id']
    search_fields = ['first_name', 'last_name', 'email']
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = User.objects.filter(company=self.request.user.company)
        return queryset


class ResendEmailVerificationView(APIView):
    '''
    This view is to resend email verification mail to activate system account.
    '''
    def post(self, request, formate=None):
        '''
        '''
        serialized_data = ResendVerificationMailSerializer(data=request.data)

        if serialized_data.is_valid():
            
            try:

                user_instance = User.objects.get(email=request.data['email'])
            
            except User.DoesNotExist:
            
                return Response({
                    "error" : "User never registered.",
                    "status" : status.HTTP_200_OK
                })
            
            if user_instance.is_email_varified == False:
                            
                otp_exist = verify_otp_exist(user_instance.id)

                if otp_exist['status'] == status.HTTP_404_NOT_FOUND:

                    otp = store_otp(otp = generate_otp(), user_instance = user_instance)

                elif otp_exist['status'] == status.HTTP_302_FOUND:

                    otp = otp_exist['otp']
                
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
    '''
    pass


class SuperUserInvite(APIView):
    '''
    Invite more super users to the system.
    '''
    def post(self, request, format=None):
        pass


class ResendSuperUserInvite(APIView):
    '''
    Resend invite mail to the invited user.
    '''
    def post(self, request, format=None):
        pass


class VerifySuperUserInvite(APIView):
    '''
    Verify the token of invited super user.
    '''
    def post(self, request, format=None):
        '''
        '''
        pass


class ConnectInstanceView(APIView):
    '''
    Help customers to connect their snowflake instances.
    '''
    def post(self, request, format=None):
        '''
        '''
        pass