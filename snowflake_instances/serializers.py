from rest_framework import serializers

from snowflake_instances.models import Instances, InstanceAccountType

from snowflake_optimizer.settings import SECRET_KEY

import jwt
import datetime


class AccountTypeSerializer(serializers.ModelSerializer):
    '''
    '''
    class Meta:
    
        model = InstanceAccountType
        fields = '__all__'


class InstancesSerializer(serializers.ModelSerializer):
    '''
    '''
    company = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    password = serializers.SerializerMethodField()
    account_type = serializers.SerializerMethodField()

    class Meta:
    
        model = Instances
    
        fields = ['id', 'instance_name', 'instance_user', 'password', 'instance_password', 'instance_role', 'company', 'instance_account', 'created_by', 'instance_account_type', 'account_type', 'last_connected']
    
        extra_kwargs = {
            'created_by' : {
                'required' : False
            },
            'company' : {
                'required' : False
            },
            'instance_password' : {
                'write_only' : True
            },
            'instance_account_type':{
                'write_only' : True
            },
            'last_connected' : {
                'read_only' : True
            }
        }
    
    def get_company(self, obj):

        company = {
            "company_id" : obj.company.id,
            "company_name" : obj.company.company_name,
        }
        
        return company

    def get_created_by(self, obj):
        
        created_by = {
            "user_id" : obj.created_by.id,
            "user_name" : obj.created_by.first_name +' '+ obj.created_by.last_name,
        }
        
        return created_by
    
    def get_password(self, obj):
    
        password = jwt.decode(obj.instance_password, SECRET_KEY, algorithms=['HS256'])

        return password['password']
    
    def get_account_type(self, obj):
        
        return {
            "id" : obj.instance_account_type.id,
            "account_type" : obj.instance_account_type.account_type
        }
    
    def update(self, instance, validated_data):

        instance.instance_name = validated_data.get('instance_name', instance.instance_name)
        instance.instance_user = validated_data.get('instance_user', instance.instance_user)
        instance.instance_password = validated_data.get('instance_password', instance.instance_password)
        instance.instance_account = validated_data.get('instance_account', instance.instance_account)
        instance.instance_account_type = validated_data.get('instance_account_type', instance.instance_account_type)
        instance.last_connected = datetime.datetime.now()

        instance.save()

        return instance
    
    def create(self, validated_data):

        validated_data['last_connected'] = datetime.datetime.now()

        return Instances.objects.create(**validated_data)