from rest_framework.views import APIView
from rest_framework.generics import  RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from system_users.models import User, EmailVerificationOtp
from system_users.serializers import RegisterUpdateUserSerializer, RetriveUserProfileSerializer, ChangePasswordSerializer, TokenObtainPairSerializer, InvitedMemberSerializer, RegisterInvitedUserSerializer
from system_users.utilities import store_otp, generate_otp, verify_otp_exist, check_request_data, check_user_group
from system_users.tasks import send_forgot_password_otp_mail

from django.db import transaction, IntegrityError
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.hashers import check_password

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

            serialized_data.validated_data['user_group'] = 'Organisation Member'

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

            serialized_data.validated_data['user_group'] = 'Super Admin'

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


class UpdateProfile(APIView):

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
    permission_classes = [IsAuthenticated]

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
                    
                invit_instance = serialized_data.save()

                return Response({
                    "message":"Invite Sent.",
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
    '''
    def post(self, request, format=None):
        '''
        '''
        pass


class ResendForgotPasswordVerificationView(APIView):
    pass


class UpdateCompanyDetaisView(APIView):
    '''
    '''
    def post(self, request, format=None):
        '''
        '''
        pass