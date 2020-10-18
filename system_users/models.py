from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import signals

from system_users.signals import user_post_save, invited_member_post_save
from system_users.manager import UserManager



class BaseModel(models.Model):
    
    '''
    '''
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CompanyDetails(BaseModel):

    '''
    This is the list of all the companies registered with the system.
    '''
    company_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self):

        return 'CompanyDetails Object ({})'.format(self.id)


class User(AbstractBaseUser, PermissionsMixin):

    '''
    This model will authentication and profiel contain information for - Merchants, Admins and Delivery Agents
    '''    
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)

    email = models.EmailField(max_length=255, blank=False, unique= True)
    mobile_number = models.BigIntegerField(blank=False, unique=True)
    
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, blank=False)
        
    password = models.TextField(blank=False, null=False)
        
    is_mobile_number_verified = models.BooleanField(default=False, blank=False, null=False)
    is_email_varified = models.BooleanField(default=False, blank=False, null=False)
    
    is_active = models.BooleanField(default=False, blank=False, null=False)

    '''
    Point the model to its custome model manager.
    '''
    objects = UserManager()

    '''
    Declare to override username to email as an authentication field.
    '''
    USERNAME_FIELD = 'email'

    def __str__(self):

        return 'User Object ({})'.format(self.id)

signals.post_save.connect(user_post_save, sender=User)


class EmailVerificationOtp(BaseModel):

    otp = models.IntegerField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):

        return 'EmailVerificationOtp Object ({})'.format(self.id)


class InvitedMembers(BaseModel):
    '''
    '''
    email = models.EmailField(max_length=255, blank=False, unique= True)
    token = models.TextField(blank=False, null=False)
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    is_onboarded = models.BooleanField(default=False, blank=False, null=False)

signals.post_save.connect(invited_member_post_save, sender=InvitedMembers)