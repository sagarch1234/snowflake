import os
import logging

from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from snowflake_optimizer.celery import app

from snowflake_instances.constants import INSTANCES_CREATED

from snowflake.instance_connector.connection import SnowflakeConnector, CloseSnowflakeConnection, DisposeEngine
from snowflake.instance_parameters.record_parameters import RecordParameters
from snowflake.instance_parameters.associate import AssociateInstance 
from snowflake.instance_parameters.initial_data_collection import  ParametersAndInstanceData

from snowflake.collect_metadata import constants, queries_and_tables
from snowflake.collect_metadata.metadata_collection import CollectMetaData

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)

@app.task
def metadata_collection(account, user, password, user_id, company_id, event, instance_id):

    meta_collection = CollectMetaData(account=account, user=user, password=password, user_id=user_id, company_id=company_id, event=event, instance_id=instance_id)

    for item in queries_and_tables.queries_tables_list:
        meta_collection.collect_process_dump(sql=item[0], table_name=item[1])

@app.task
def parameters_and_instance_data(user, password, account, instance_id, user_id, company_id, event):

    parameters_and_instance_data = ParametersAndInstanceData(user, password, account, instance_id, user_id, company_id, event)

    account_level = parameters_and_instance_data.account_level_etl()

    databases = parameters_and_instance_data.databases_etl()

    schema = parameters_and_instance_data.schema_etl()

    schema_level = parameters_and_instance_data.schema_level_etl()

    database_level = parameters_and_instance_data.databases_level_etl()

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