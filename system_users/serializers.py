from rest_framework import serializers

from system_users.models import User, CompanyDetails, InvitedMembers

from django.contrib.auth.models import Group
from django.db import transaction

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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


class RegisterInvitedUserSerializer(serializers.ModelSerializer):
    '''
    This serializer is for Register User view.
    '''
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'mobile_number', 'password']
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
            'mobile_number' : {
                'required' : True,
            },
            'password' : {
                'required' : True,
                'allow_blank' : False,
                'allow_null' : False,
                'write_only': True,
                'read_only':False
            }
        }
    
    @transaction.atomic
    def create(self, validated_data):

        company = validated_data.pop('company')

        user_group = validated_data.pop('user_group')

        user_group = Group.objects.get(name=user_group)

        company = CompanyDetails.objects.get(company_name=company)

        validated_data['company'] = company

        user = User.objects.create_user(**validated_data)

        user_and_group = user.groups.add(user_group)

        update_invite_onboarding = InvitedMembers.objects.get(email=user.email)
        update_invite_onboarding.is_onboarded = True
        update_invite_onboarding.save()
        
        return user


class UpdateCompanyDetailsSerializer(serializers.ModelSerializer):
    '''
    '''
    pass


class TokenObtainPairSerializer(TokenObtainPairSerializer):
    '''
    This serializer is used by TokenObtainPairView.
    This serializer was created to add an extra key value pair to the login response.
    '''

    def validate(self, attrs):

        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        data['group'] = list(self.user.groups.values('id', 'name'))

        return data


class RegisterUpdateUserSerializer(serializers.ModelSerializer):
    '''
    This serializer is for Register User view.
    '''
    company = CompanyDetailsSerializer()
    user_group = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'mobile_number', 'company', 'password','user_group']
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
                'write_only': True,
                # 'editable':False,
                'read_only':False
            }
        }
    def get_user_group(self, obj):
        return list(obj.groups.values('id', 'name'))

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

    def update(self, instance, validated_data):

        # if 'company' in validated_data:
            
        #     company_data = validated_data.pop('company')
            
        #     company_instance = instance.company

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile_number = validated_data.get('mobile_number', instance.mobile_number)

        # company_instance.company_name = company_data.get('company_name', company_instance.company_name)
        
        instance.save()
        # company_instance.save()

        return instance


class RetriveUserProfileSerializer(serializers.ModelSerializer):
    '''
    This serializer is to retrive user profile.
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


class ChangePasswordSerializer(serializers.Serializer):
    '''
    This serializer is for system user to update the password when they ae logged in.
    '''
    current_password = serializers.CharField(max_length=255, allow_blank=False, required=True, allow_null=False)
    new_password = serializers.CharField(max_length=255, allow_blank=False, required=True, allow_null=False)

    def update(self, instance, validated_data):

        validated_data.pop('current_password')

        if 'new_password' in validated_data:
            password = validated_data.pop('new_password')
            instance.set_password(password)

        instance.new_password = validated_data.get('password', instance.password)
        
        instance.save(update_fields=['password'])

        return instance


class InvitedMemberSerializer(serializers.ModelSerializer):
    '''
    '''
    
    invited_by = serializers.SerializerMethodField()

    class Meta:
        model = InvitedMembers
        fields = ['email', 'is_onboarded', 'token', 'invited_by']
        extra_kwargs = {
            'email' : {
                'required' : True
            },
            'token' : {
                'required' : True,
                'write_only' : True
            }
        }
    
    def get_invited_by(self, obj):

        invited_by = {
            'name' : obj.invited_by.first_name + ' ' + obj.invited_by.last_name,
        }

        return invited_by
    
    def update(self, instance, validated_data):
        instance.token = validated_data.get('token', instance.token)
        instance.save(update_fields=['token'])
        return instance

    