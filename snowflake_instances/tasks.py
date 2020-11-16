from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from snowflake_optimizer.celery import app

from snowflake_instances.constants import INSTANCES_CREATED

from snowflake.instance_connector.connection import SnowflakeConnector, CloseSnowflakeConnection, DisposeEngine
from snowflake.instance_connector.record_parameters import RecordParameters

import os


@app.task
def parameters_and_instance_data(user, password, account):

    #connect to instance
    instance = SnowflakeConnector(user, password, account, 'ACCOUNTADMIN')
    connection = instance.connect_snowflake_instance()

    #create an object for class RecordParameters.
    record_params = RecordParameters(connection['connection_object'])

    #fetch accout level parameters.
    account_level = record_params.account_level()

    #fetch databases.
    get_databases = record_params.get_databases()

    #fetch database level parameters.
    database_level = record_params.database_level()

    #close instance connection
    close_instance = CloseSnowflakeConnection(connection['connection_object'])
    close_instance.close_connected_instance()             

    #dispose engine
    dispose_engine = DisposeEngine(connection['engine'])
    dispose_engine.close_engine()



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