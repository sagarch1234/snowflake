import sys
import os
sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')

from connection import SnowflakeConnector
from queries_and_tables import queries_tables_list
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
        self.sfo_con = self.sfo_connector.connect_snowflake_instance()

        #get data object
        self.get_data = GetCustomerData(self.customer_engine)

        #associate data object
        self.associate = AssociateData(instance_id=self.instance_id, user_id=self.user_id, event=self.event, company_id=self.company_id)

        #load data 
        self.load_data = LoadData(engine=self.sfo_engine, connection=self.sfo_con)

    
    def collect_process_dump(self, sql, table_name, index_label):

        if table_name == constants.TABLE_ACCOUNT_PARAMETERS:

            account_parameters_df = self.get_data.get_data(sql=sql, database_name = None, database_schema = None)

            associated_data_df = self.associate.associate_data(account_parameters_df)
        
        elif table_name == constants.TABLE_DATABASES:

            instance_databases_df = self.get_data.get_data(sql=sql, database_name = None, database_schema = None)
            associated_data_df = self.associate.associate_data(instance_databases_df)
        
        elif table_name == constants.TABLE_SCHEMAS:

            instance_schemas_df = self.get_data.get_data(sql=sql, database_name = None, database_schema = None)
            associated_data_df = self.associate.associate_data(instance_schemas_df)
        
        elif table_name == constants.TABLE_DB_LEVEL_PARAMETERS:

            instance_databases_df = self.get_data.get_data(sql=constants.SQL_DATABASES, database_name = None, database_schema = None)
            
            final_db_level_paramaters_df = pd.DataFrame()
            
            for database in instance_databases_df['name']:

                sql = sql.format(database)

                db_level_parameters_df = self.get_data.get_data(sql=sql, database_name = database, database_schema = None)

                db_level_parameters_df['database_name'] = database
                
                final_db_level_paramaters_df.append(db_level_parameters_df)

            associated_data_df = self.associate.associate_data(final_db_level_paramaters_df)

        elif table_name == constants.TABLE_SCHEMA_PARAMETERS:

            final_schema_parameters_df = pd.DataFrame()

            instance_schemas_df = self.get_data.get_data(sql=constants.SQL_SCHEMAS, database_name = None, database_schema = None)
            
            instance_databases_df = self.get_data.get_data(sql=constants.SQL_DATABASES, database_name = None, database_schema = None)

            for database in instance_databases_df['name']:
                                
                sql_query = constants.SQL_SCHEMAS_IN_DATABASES.format(database)
                
                instance_schemas_df = self.get_data.get_data(sql=sql_query, database_name = database, database_schema = None)
                
                for schema in instance_schemas_df['name']:

                    sql = sql.format(database, schema)
                
                    schema_parameters_df = self.get_data.get_data(sql=sql, database_name = database, database_schema = schema)
                    
                    schema_parameters_df['schema_name'] = schema
                    schema_parameters_df['database_name'] = database
                    
                    final_schema_parameters_df = final_schema_parameters_df.append(schema_parameters_df)
                    
            associated_data_df = self.associate.associate_data(final_schema_parameters_df)

        self.load_data.dump_data(table_name=table_name, dataframe=associated_data_df, index_label=index_label)






# temp = CollectParametersData(account='lt90919.us-central1.gcp', user='shivkant', password='Shiva@123!!*', user_id=2, company_id=4, event="Add Instance", instance_id=4)

# temp.collect_process_dump(sql =constants.SQL_ACCOUNT_PARAMETERS , table_name = constants.TABLE_ACCOUNT_PARAMETERS)

# for query_table in queries_tables_list:
    
    # temp.collect_process_dump(sql =query_table[0] , table_name = query_table[1], index_label=query_table[2])