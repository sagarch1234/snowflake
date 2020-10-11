from rest_framework import serializers
from system_users.models import User, CompanyDetails

from django.contrib.auth.models import Group

from django.db import transaction

from system_users.utilities import verify_otp_exist

from rest_framework import status


class CompanyDetailsSerializer(serializers.ModelSerializer):
    '''
    This class has been extended by RegisterUserSerializer.
    '''
    class Meta:
        model = CompanyDetails
        fields = ['id', 'company_name', 'is_active']
        extra_kwargs = {
            'company_name' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            }
        }


class RegisterUserSerializer(serializers.ModelSerializer):
    '''
    This serializer is for Register User view.
    '''
    company = CompanyDetailsSerializer()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'mobile_number', 'company', 'password']
        extra_kwargs = {
            'first_name' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            },
            'last_name' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            },
            'email' : {
                'required' : True,
                'allow_null' : False,
                'allow_blank' : False
            },
            'mobile_number' : {
                'required' : True,
            },
            'password' : {
                'required' : True,
                'allow_blank' : False,
                'allow_null' : False,
                'write_only': True
            }
        }
    
    @transaction.atomic
    def create(self, validated_data):

        company = validated_data.pop('company')

        user_group = validated_data.pop('user_group')

        user_group = Group.objects.get(name=user_group)

        company = CompanyDetails.objects.create(**company)

        validated_data['company'] = company

        user = User.objects.create_user(**validated_data)

        user_and_group = user.groups.add(user_group)
        
        return user


class RetriveUserProfileSerializer(serializers.ModelSerializer):

    '''
    '''
    company_name = serializers.SerializerMethodField()
    user_group = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile_number', 'company_name', 'user_group']
    
    def get_company_name(self, obj):

        return obj.company.company_name
    
    def get_user_group(self, obj):

        user_group_object_list = list(obj.groups.values('id', 'name'))

        return user_group_object_list