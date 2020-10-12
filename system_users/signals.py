from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from system_users.tasks import send_email_verification_mail, send_account_activation_mail, send_password_updated_mail, send_forgot_password_otp_mail
from system_users.utilities import store_otp, generate_otp, verify_otp_exist

from rest_framework import status

from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created

import socket


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.first_name,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}{}/?token={}".format(reverse('password_reset:reset-password-request'), 'confirm', reset_password_token.key)
    }

    send_forgot_password_otp_mail.delay(first_name=context['username'], email=context['email'], otp = context['reset_password_url'])


def user_post_save(sender, instance, created, signal, *args, **kwargs):

    if not created:
        print(type(kwargs['update_fields']))
        
        if kwargs['update_fields'] is None:

            print('No updated fields.')

        else:

            if (('is_active' in  kwargs['update_fields']) and ('is_email_varified' in  kwargs['update_fields'])):
                
                send_account_activation_mail.delay(first_name=instance.first_name, email=instance.email)
            
            if 'password' in kwargs['update_fields']:

                send_password_updated_mail.delay(first_name=instance.first_name, email=instance.email)

    if created:

        otp_exist = verify_otp_exist(instance.id)

        if otp_exist['status'] == status.HTTP_404_NOT_FOUND:

            otp = store_otp(otp = generate_otp(), user_instance = instance)

        elif otp_exist['status'] == status.HTTP_302_FOUND:

            otp = otp_exist['otp']
        
        send_email_verification_mail.delay(first_name=instance.first_name, otp=otp, email=instance.email)

        
            