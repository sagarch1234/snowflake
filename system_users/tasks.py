from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from snowflake_optimizer.celery import app

import os

@app.task
def send_email_verification_mail(first_name, otp, email):

    template = 'email_verification.html'

    subject =  'Verify your email to activate your account.'

    body = render_to_string(
        template, {
            'fist_name' : first_name,
            'otp' : otp
        }
    )

    plain_body = strip_tags(body)

    sender = os.environ.get('EMAIL_HOST_USER')

    to = email

    mail_status = send_mail(subject, plain_body, sender, [to], html_message=body, fail_silently=False,)