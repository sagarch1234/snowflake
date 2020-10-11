from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from system_users.tasks import send_email_verification_mail

from system_users.utilities import store_otp, generate_otp, verify_otp_exist

from rest_framework import status


def user_post_save(sender, instance, created, signal, *args, **kwargs):

    if created:

        # call store otp method.

        otp_exist = verify_otp_exist(instance.id)

        if otp_exist['status'] == status.HTTP_404_NOT_FOUND:

            otp = store_otp(otp = generate_otp(), user_instance = instance)

        elif otp_exist['status'] == status.HTTP_302_FOUND:

            otp = otp_exist['otp']
        
        print("OTP>>>>>>>>>>>",otp)

        send_email_verification_mail.delay(first_name=instance.first_name, otp=otp, email=instance.email)

        
            