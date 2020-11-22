import sys

sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')
sys.path.insert(1,  '/snowflake-backend/snowflake/instance_parameters')

from connection import SnowflakeConnector
from record_parameters import RecordParameters
from  modals import AccountParameters, DatabasesOnInstance, SchemaOnInstance

from sqlalchemy.orm import sessionmaker

import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)


class DumpParameters():

    def __init__(self, engine, account_parameters=None, databases=None, schema=None):
        self.account_parameters = account_parameters
        self.databases = databases
        self.schema = schema
        self.engine = engine
        self.Session = sessionmaker(bind=engine)

    def dump_account_parameters(self):

        session = self.Session()
                
        account_parameter_obj = []

        for account_parameter in self.account_parameters:

            account_parameter_obj.append(AccountParameters(key=account_parameter[0], value=account_parameter[1], default=account_parameter[2], level=account_parameter[3], description=account_parameter[4], type=account_parameter[5], instance_id=account_parameter[6]))

        session.add_all(account_parameter_obj)

        try:

            x = session.commit()
        
        except Exception as identifier:
        
            logging.error(identifier)
        
        logging.info("Account Parameters dumped to snowflakes databases.")

        return True
    
    def dump_databases(self):

        session = self.Session()
                
        database_obj = []

        for database in self.databases:

            database_obj.append(DatabasesOnInstance(created_on=database[0], name=database[1], is_default=database[2], is_current=database[3], origin=database[4], owner=database[5], comment=database[6], options=database[7], retention_time=database[8], instance_id=database[9]))

        session.add_all(database_obj)

        try:

            x = session.commit()
        
        except Exception as identifier:
        
            logging.error(identifier)
        
        logging.info("Databases dumped to snowflakes databases.")

        # return True
        
    def dump_database_level(self):
        pass
    
    def dump_schema(self):

        session = self.Session()
                
        schema_obj = []

        for each_schema in self.schema:

            schema_obj.append(SchemaOnInstance(created_on=each_schema[0], name=each_schema[1], is_default=each_schema[2], is_current=each_schema[3], database_name=each_schema[4], owner=each_schema[5], comment=each_schema[6], options=each_schema[7], retention_time=each_schema[8], instance_id=each_schema[9]))

        session.add_all(schema_obj)

        try:

            x = session.commit()
        
        except Exception as identifier:
        
            logging.error(identifier)
        
        logging.info("Schemas dumped to snowflakes databases.")

        return True
    
    def dump_schema_level(self):
        pass



