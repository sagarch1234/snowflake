from rest_framework.permissions import BasePermission

from system_users.models import InvitedMembers, User
from system_users.constants import SUPER_ADMIN

from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404



class IsInviteOwner(BasePermission):
    '''
    '''
    def has_object_permission(self, request, view):
        '''
        '''
        try:
            invited_by = InvitedMembers.objects.get(pk=request.query_params['invite_id']).invited_by.id
        except InvitedMembers.DoesNotExist:
            invited_by = 0
        
        return request.user.id == invited_by


class WhitelistCompanyAdmin(BasePermission):
    '''
    '''
    def has_permission(self, request, view):
        '''
        '''
        user = get_object_or_404(User, pk=request.user.id)

        current_user_group = list(request.user.groups.values('name'))
        
        return str(Group.objects.get(name=SUPER_ADMIN)) == current_user_group[0]['name']