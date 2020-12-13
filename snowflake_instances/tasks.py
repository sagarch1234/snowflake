import os
import logging

from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from snowflake_optimizer.celery import app

from snowflake_instances.constants import INSTANCES_CREATED

from snowflake.instance_connector.connection import SnowflakeConnector, CloseSnowflakeConnection, DisposeEngine

from snowflake.collect_metadata import constants, queries_and_tables
from snowflake.collect_metadata.metadata_collection import CollectMetaData

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)


@app.task
def send_instance_added_mail(organisation_name, email, created_by, instance_name):

    template = 'instance_created.html'

    subject =  INSTANCES_CREATED

    body = render_to_string(
        template, {
            'organisation_name' : organisation_name,
            'created_by' :  created_by,
            'instance_name':instance_name
        }
    )

    plain_body = strip_tags(body)

    sender = os.environ.get('EMAIL_HOST_USER')

    to = email

    mail_status = send_mail(subject, plain_body, sender, to, html_message=body, fail_silently=False,)