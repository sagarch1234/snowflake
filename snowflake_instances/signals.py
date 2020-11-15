from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from snowflake_instances.tasks import send_instance_added_mail

from system_users.models import User

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)



def new_instance_added_mail(sender, instance, created, signal, *args, **kwargs):

    if created:

        created_by = instance.created_by.first_name + ' ' + instance.created_by.last_name
        
        queryset = list(User.objects.filter(company=instance.company.id, is_active=True))
        
        email = []

        for each_email in queryset:
            email.append(each_email.email)

        send_instance_added_mail.delay(organisation_name=instance.company.company_name, email=email, created_by=created_by, instance_name=instance.instance_name)
    