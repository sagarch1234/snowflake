from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import  RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from system_users.models import User
from system_users.serializers import RegisterUserSerializer, RetriveUserProfileSerializer

from django.db import transaction


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

        serialized_data = RegisterUserSerializer(data=request.data)

        if serialized_data.is_valid():

            serialized_data.validated_data['is_mobile_number_verified'] = False
            serialized_data.validated_data['is_email_varified'] = False
            serialized_data.validated_data['is_active'] = False

            serialized_data.validated_data['user_group'] = 'Admin'
            
            user = serialized_data.save()
        
        else:
        
            return Response(serialized_data.errors)

        if user == None:

            return Response({
                "message" : "Oppsss.. something went wrong.",
                "status" : status.HTTP_409_CONFLICT
            })

        else:

            return Response({
                "message":"Verification mail has been sent to your email " + request.data['email'] +  ". Please provide the OTP to verify your email and active your account. " ,
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


class ChangePasswordView(APIView):

    '''
    This view will help user change their current password.

    Authentication is required for this view.
    '''
    pass