from rest_framework import serializers

from snowflake_connector.models import Instances


class InstancesSerializer(serializers.ModelSerializer):
    '''
    '''
    class Meta:
        model = Instances
        fields = ['id', 'instance_name', 'instance_user', 'instance_password', 'instance_role', 'company', 'instance_account', 'created_by']
        extra_kwargs = {
            'created_by' : {
                'required' : False
            }
        }