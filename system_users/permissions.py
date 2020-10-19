from rest_framework.permissions import BasePermission

from system_users.models import InvitedMembers, User


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