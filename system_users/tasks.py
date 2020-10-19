from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from snowflake_optimizer.celery import app

from system_users.constants import LOGIN_URL, FORGOT_PASSWORD, FORGOT_PASSWORD_SUBJECT, ACCOUNT_PASSWORD_UPDATED, ACCOUNT_ACTIVATED, EMAIL_VERIFICATION, INVITE_MEMBER

import os


@app.task
def send_member_invite_mail(organisation_name, email, token, invited_by):

    template = 'member_invite.html'

    subject =  INVITE_MEMBER

    body = render_to_string(
        template, {
            'organisation_name' : organisation_name,
            'end_point' : "127.0.0.1:8080/api/users/invite-member/" + token,
            'invited_by' : invited_by 
        }
    )

    plain_body = strip_tags(body)

    sender = os.environ.get('EMAIL_HOST_USER')

    to = email

    mail_status = send_mail(subject, plain_body, sender, [to], html_message=body, fail_silently=False,)


@app.task
def send_email_verification_mail(first_name, otp, email):

    template = 'email_verification.html'

    subject =  EMAIL_VERIFICATION

    body = render_to_string(
        template, {
            'first_name' : first_name,
            'otp' : otp
        }
    )

    plain_body = strip_tags(body)

    sender = os.environ.get('EMAIL_HOST_USER')

    to = email

    mail_status = send_mail(subject, plain_body, sender, [to], html_message=body, fail_silently=False,)


@app.task
def send_account_activation_mail(first_name, email):

    template = 'account_activation.html'

    subject =  ACCOUNT_ACTIVATED

    body = render_to_string(
        template, {
            'first_name' : first_name,
            'login_page' : LOGIN_URL
        }
    )

    plain_body = strip_tags(body)

    sender = os.environ.get('EMAIL_HOST_USER')

    to = email

    mail_status = send_mail(subject, plain_body, sender, [to], html_message=body, fail_silently=False,)


@app.task
def send_password_updated_mail(first_name, email):

    template = 'password_changed.html'

    subject =  ACCOUNT_PASSWORD_UPDATED

    body = render_to_string(
        template, {
            'first_name' : first_name
            }
    )

    plain_body = strip_tags(body)

    sender = os.environ.get('EMAIL_HOST_USER')

    to = email

    mail_status = send_mail(subject, plain_body, sender, [to], html_message=body, fail_silently=False,)


@app.task
def send_forgot_password_otp_mail(first_name, otp, email):

    template = 'forgot_password_otp.html'

    subject =  FORGOT_PASSWORD_SUBJECT

    body = render_to_string(
        template, {
            'first_name' : first_name,
            'otp' : otp,
            'forgot_password' : FORGOT_PASSWORD
        }
    )

    plain_body = strip_tags(body)

    sender = os.environ.get('EMAIL_HOST_USER')

    to = email

    mail_status = send_mail(subject, plain_body, sender, [to], html_message=body, fail_silently=False,)
