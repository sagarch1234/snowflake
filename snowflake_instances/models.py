from django.db import models

from django.db.models import signals

from system_users.models import BaseModel, CompanyDetails, User


class InstanceAccountType(models.Model):
    account_type = models.CharField(max_length=255, null=False, blank=False)


class Instances(BaseModel):
    '''
    '''
    instance_name = models.CharField(max_length=50, null=False, blank=False)
    instance_user = models.CharField(max_length=50, null=False, blank=False)
    instance_password = models.TextField( null=False, blank=False)
    instance_role = models.CharField(max_length=50, default='ACCOUNTADMIN', null=False, blank=False)
    instance_account = models.CharField(max_length=200, unique=True, null=False, blank=False)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=False, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    instance_account_type = models.ForeignKey(InstanceAccountType, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):

        return 'Instances Object ({})'.format(self.id)
