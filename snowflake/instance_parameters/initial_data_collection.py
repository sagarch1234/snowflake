import sys
import os

sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')
sys.path.insert(1,  '/snowflake-backend/snowflake/instance_parameters')

from connection import SnowflakeConnector
from record_parameters import RecordParameters
from associate import  AssociateInstance
from  load_parameters import DumpParameters

import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)

class ParametersAndInstanceData():

    def __init__(self, user, password, account, instance_id, user_id, company_id, event):

        #create an object for class SnowflakeConnector.
        self.customer_connection_instance = SnowflakeConnector(user=user, password=password, account=account, role='ACCOUNTADMIN')

        #establish connection with the customer's snowflake instance.
        self.customer_connection = self.customer_connection_instance.connect_snowflake_instance()
        
        #create an object for class RecordParameters.
        self.record_params = RecordParameters(self.customer_connection['connection_object'])
        
        self.instance_id = instance_id

        self.sfo_connection_instance = SnowflakeConnector(user=os.environ.get('SNOWFLAKE_ACCOUNT_USER'), password=os.environ.get('SNOWFLAKE_ACCOUNT_PASSWORD'), account=os.environ.get('SNOWFLAKE_ACCOUNT'), database_name=os.environ.get('SNOWFLAKE_DATABASE_NAME'), schema_name=os.environ.get('SCHEMA_NAME'), role=os.environ.get('ACCOUNT_ROLE'), warehouse=os.environ.get('ACCOUNT_WAREHOUSE'))

        self.sfo_engine = self.sfo_connection_instance.get_engine()

        self.user_id = user_id

        self.company_id = company_id
        
        self.event = event

    def account_level_etl(self):

        #fetch accout level parameters.
        account_level = self.record_params.account_level()

        #create associate class instance.
        associate_instance = AssociateInstance(instance_id=self.instance_id, user_id=self.user_id, company_id=self.company_id, event=self.event, account_parameters=account_level)

        #associate account_level with instance
        associated_instance = associate_instance.associate_instance_to_account_parameters()

        #create DumpParameters class instance.
        dump_parameters = DumpParameters(engine=self.sfo_engine, account_parameters=associated_instance)

        #dump data
        dump_parameters.dump_account_parameters()

        # return True
    
    def databases_etl(self):

        #fetch databases.
        databases = self.record_params.get_databases()

        #create associate class instance.
        associate_instance = AssociateInstance(instance_id=self.instance_id, databases=databases, user_id=self.user_id, company_id=self.company_id, event=self.event)

        #associate account_level with instance
        associated_instance = associate_instance.associate_instance_to_databases()

        #create DumpParameters class instance.
        dump_parameters = DumpParameters(engine=self.sfo_engine, databases=associated_instance)

        #dump data
        dump_parameters.dump_databases()
    
    def schema_etl(self):

        #fetch schema.
        schemas = self.record_params.get_schema()

        #create associate class instance.
        associate_instance = AssociateInstance(instance_id=self.instance_id, schema=schemas,  user_id=self.user_id, company_id=self.company_id, event=self.event)

        #associate account_level with instance
        associated_instance = associate_instance.associate_instance_to_schema()

        #create DumpParameters class instance.
        dump_parameters = DumpParameters(engine=self.sfo_engine, schema=associated_instance)

        #dump data
        dump_parameters.dump_schema()
    
    def databases_level_etl(self):

        #fetch database level parameters.
        database_level_parameters = self.record_params.database_level()

        #create associate class instance.
        associate_instance = AssociateInstance(instance_id=self.instance_id, database_level=database_level_parameters,  user_id=self.user_id, company_id=self.company_id, event=self.event)
        
        associated_data = associate_instance.associate_instance_to_database_level()

        dump_parameters = DumpParameters(database_level=associated_data, engine=self.sfo_engine)
        dump_parameters.dump_database_level()

    def schema_level_etl(self):

        #fetch schema level parameters.
        schema_level = self.record_params.schema_level()

        #create associate class instance.
        associate_instance = AssociateInstance(instance_id=self.instance_id, schema_level=schema_level,  user_id=self.user_id, company_id=self.company_id, event=self.event)
        associated_data = associate_instance.associate_instance_to_schema_level()

        dump_parameters = DumpParameters(schema_level=associated_data, engine=self.sfo_engine)
        dump_parameters.dump_schema_level()

