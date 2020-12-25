import sys
import os
sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')

import snowflake.connector
from queries_and_tables import queries_tables_list
from connection import SnowflakeConnector

from get_data import GetCustomerData
from load_data import LoadData
from associate_data import AssociateData

from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine



class CollectMetaData():
    def __init__(self, account, user, password, user_id, company_id, event, instance_id):

        #other arguments for associate data.
        self.instance_id = instance_id
        self.event = event
        self.company_id = company_id
        self.user_id = user_id

        #connect to customer snowflake instance
        self.customer_engine = create_engine(URL(account = account, user = user, password = password, role='ACCOUNTADMIN'))
        self.customer_connector = self.customer_engine.connect()
        
        #connect to SFO's snowflake instance
        self.sfo_connector = SnowflakeConnector(user=os.environ.get('SNOWFLAKE_ACCOUNT_USER'), password=os.environ.get('SNOWFLAKE_ACCOUNT_PASSWORD'), account=os.environ.get('SNOWFLAKE_ACCOUNT'), database_name=os.environ.get('SNOWFLAKE_DATABASE_NAME'), schema_name=os.environ.get('SCHEMA_NAME_AUDITS'), role=os.environ.get('ACCOUNT_ROLE'), warehouse=os.environ.get('ACCOUNT_WAREHOUSE'))
        self.sfo_engine = self.sfo_connector.get_engine()
        self.sfo_con = self.sfo_connector.connect_snowflake_instance()

        #get data object
        self.get_data = GetCustomerData(self.customer_engine)

        #associate data object
        self.associate = AssociateData(instance_id=self.instance_id, user_id=self.user_id, event=self.event, company_id=self.company_id)

        #load data 
        self.load_data = LoadData(engine=self.sfo_engine, connection=self.sfo_con)
        
        
    def collect_process_dump(self, sql, table_name, index_label):

        #get_data
        customer_df = self.get_data.get_data(sql)

        #associate_data
        associate_df = self.associate.associate_data(dataframe=customer_df)

        #load_data
        load_data = self.load_data.dump_data(table_name=table_name, dataframe=associate_df, index_label=index_label)


# x = CollectMetaData(account='lt90919.us-central1.gcp', user='shivkant', password='Shiva@123!!*', user_id=2, company_id=4, event="AUDITS", instance_id=4)
# x.collect_process_dump(sql='SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.LOGIN_HISTORY;', table_name='account_usage_login_history')

# for queries_tables in queries_tables_list:

    # print("?????????????????????????????????/",queries_tables)

    # x.collect_process_dump(sql=queries_tables[0], table_name=queries_tables[1], index_label=queries_tables[2])