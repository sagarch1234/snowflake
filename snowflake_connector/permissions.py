from rest_framework.permissions import BasePermission

from system_users.models import User
from system_users.constants import ORGANISATION_MEMBER, SUPER_ADMIN, ORGANISATION_ADMIN

from snowflake_connector.models import Instances

from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404


class IsInstanceAccessible(BasePermission):
    '''
    This permission class will make sure, the authenticated user trying to access the instance and the instance being accessed by
    the authenticated user belong to the same company. 
    '''
    def has_object_permission(self, request, view):
        '''
        '''
        try:
            company_id = Instance.objects.get(pk=request.query_params['instance_id']).company.id
        except Instance.DoesNotExist:
            return False
        
        return request.user.company.id == company_id
