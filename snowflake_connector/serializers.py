from rest_framework import serializers

from snowflake_connector.models import Instances


class InstancesSerializer(serializers.ModelSerializer):
    '''
    '''
    company = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    class Meta:
        model = Instances
        fields = ['id', 'instance_name', 'instance_user', 'instance_password', 'instance_role', 'company', 'instance_account', 'created_by']
        extra_kwargs = {
            'created_by' : {
                'required' : False
            },
            'instance_password' : {
                'write_only' : True
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