import sys
import os
sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')

from connection import SnowflakeConnector

from get_data import GetCustomerData
from load_data import LoadData
from associate_data import AssociateData

from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import pandas as pd

import constants


class CollectParametersData():
    def __init__(self, account, user, password, user_id, company_id, event, instance_id):

        self.instance_id = instance_id
        self.event = event
        self.user_id = user_id
        self.company_id = company_id

        #connect to customer snowflake instance
        self.customer_engine = create_engine(URL(account = account, user = user, password = password, role='ACCOUNTADMIN'))
        self.customer_connector = self.customer_engine.connect()
        
        #connect to SFO's snowflake instance
        self.sfo_connector = SnowflakeConnector(user=os.environ.get('SNOWFLAKE_ACCOUNT_USER'), password=os.environ.get('SNOWFLAKE_ACCOUNT_PASSWORD'), account=os.environ.get('SNOWFLAKE_ACCOUNT'), database_name=os.environ.get('SNOWFLAKE_DATABASE_NAME'), schema_name=os.environ.get('SCHEMA_NAME_PARAMS'), role=os.environ.get('ACCOUNT_ROLE'), warehouse=os.environ.get('ACCOUNT_WAREHOUSE'))
        self.sfo_engine = self.sfo_connector.get_engine()

        #get data object
        self.get_data = GetCustomerData(self.customer_engine)

        #associate data object
        self.associate = AssociateData(instance_id=self.instance_id, user_id=self.user_id, event=self.event, company_id=self.company_id)

        #load data 
        self.load_data = LoadData(engine=self.sfo_engine)

    
    def collect_process_dump(self, sql, table_name):

        
        final_data_df = pd.DataFrame()
        #final dataframes for db level query
        final_db_level_df = pd.DataFrame()

        #final dataframe for schema level query
        final_db_schema_level_df = pd.DataFrame()

        if table_name == constants.TABLE_DATABASE_PARAMETERS:
            
            #final dataframe for databases
            final_data_df = pd.read_sql_query(sql, self.customer_engine)
            
        elif table_name == constants.TABLE_SCHEMA_PARAMETERS:
            
            #final dataframe for schemas
            final_data_df = pd.read_sql_query(sql, self.customer_engine)
            
        elif table_name == constants.TABLE_ACCOUNT_PARAMETERS:

            #final dataframe for account parameters
            final_data_df = pd.read_sql_query(sql, self.customer_engine)
        
        elif table_name == constants.TABLE_DB_LEVEL_PARAMETERS:
            for database in databases_df['name']:
                final_data_df = self.get_data.get_data(sql,database_name=database )
                #final_db_level_df.append(db_level_df)
                final_data_df['database_name'] = databases_df['name']

        elif table_name == constants.TABLE_SCHEMA_LEVEL_PARAMETERS:

            for database in databases_df['name']:
            
                for schema in schemas_df['name']:
            
                    final_data_df = self.get_data.get_data(sql, database_name=database, database_schema=schema)
            
                    #final_db_schema_level_df.append(schema_level_df)
                    final_data_df['database_name'] = databases_df['name']
                    final_data_df['schema_name'] = schemas_df['name']



        #Associate data
        associated_databases_df = self.associate.associate_data(final_data_df)


        #load data
        load_database_df = self.load_data.dump_data(table_name, final_data_df)




# temp = CollectParametersData(account='lt90919.us-central1.gcp', user='shivkant', password='Shiva@123!!*', user_id=2, company_id=4, event="Add Instance", instance_id=4)
# temp.collect_process_dump(sql = 'SHOW PARAMETERS IN ACCOUNT;' , table_name = 'account_parameters')