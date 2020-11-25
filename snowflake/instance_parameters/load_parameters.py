import sys

sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')
sys.path.insert(1,  '/snowflake-backend/snowflake/instance_parameters')

from connection import SnowflakeConnector
from record_parameters import RecordParameters
from  modals import AccountParameters, DatabasesOnInstance, SchemaOnInstance, ParametersInDatabase, ParametersInSchemas

from sqlalchemy.orm import sessionmaker
# from sqlalchemy.sql import insert

import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)


class DumpParameters():

    def __init__(self, engine, account_parameters=None, databases=None, schema=None, database_level=None, schema_level=None):
        self.account_parameters = account_parameters
        self.databases = databases
        self.schema = schema
        self.engine = engine
        self.Session = sessionmaker(bind=engine)
        self.database_level = database_level
        self.schema_level = schema_level

    def dump_account_parameters(self):

        session = self.Session()
                
        account_parameter_obj = []

        for account_parameter in self.account_parameters:

            account_parameter_obj.append(AccountParameters(key=account_parameter[0], value=account_parameter[1], default=account_parameter[2], level=account_parameter[3], description=account_parameter[4], type=account_parameter[5], instance_id=account_parameter[6], company_id=account_parameter[7], user_id=account_parameter[8], event=account_parameter[9]))

        session.add_all(account_parameter_obj)

        try:

            session.commit()
        
        except Exception as identifier:
        
            logging.error(identifier)
        
        logging.info("Account Parameters dumped to snowflakes databases.")

        return True
    
    def dump_databases(self):

        session = self.Session()
                
        database_obj = []

        for database in self.databases:

            created_on = str(database[0])
            database_model_instance = DatabasesOnInstance(created_on=created_on, name=database[1], is_default=database[2], is_current=database[3], origin=database[4], owner=database[5], comment=database[6], options=database[7], retention_time=database[8], instance_id=database[9], company_id=database[10], user_id=database[11], event=database[12])

            database_obj.append(database_model_instance)

        session.add_all(database_obj)

        try:

            session.commit()
        
        except Exception as identifier:
        
            logging.error(identifier)
        
        logging.info("Databases dumped to snowflakes databases.")
        
    def dump_database_level(self):

        session = self.Session()
                
        database_level_obj = []

        for row in self.database_level:

            database_level_modal_instance = ParametersInDatabase(key=row[0], value=row[1], default=row[2], level=row[3], description=row[4], type=row[5], database_name=row[6], instance_id=row[7],  company_id=row[8], user_id=row[9], event=row[10])

            database_level_obj.append(database_level_modal_instance)

        session.add_all(database_level_obj)

        try:

            session.commit()
        
        except Exception as identifier:
        
            logging.error(identifier)
        
        logging.info("Databases level dumped to snowflakes databases.")
    
    def dump_schema(self):

        session = self.Session()
                
        schema_obj = []

        print(self.schema)

        for each_schema in self.schema:

            created_on = str(each_schema[0])

            schema_modal_instance = SchemaOnInstance(created_on=each_schema[0], name=each_schema[1], is_default=each_schema[2], is_current=each_schema[3], database_name=each_schema[4], owner=each_schema[5], comment=each_schema[6], options=each_schema[7], retention_time=each_schema[8], instance_id=each_schema[9], company_id=each_schema[10], user_id=each_schema[11], run_date_time=each_schema[12], event=each_schema[13])

            schema_obj.append(schema_modal_instance)

        session.add_all(schema_obj)

        try:

            session.commit()
        
        except Exception as identifier:
        
            logging.error(identifier)
        
        logging.info("Schemas dumped to snowflakes databases.")
    
    def dump_schema_level(self):

        session = self.Session()
        
        schema_level_object = []

        for row in self.schema_level:

            schema_level = ParametersInSchemas(key=row[0], value=row[1], default=row[2], level=row[3], description=row[4], type=row[5], database_name=row[6], schema_name=row[7], instance_id=[8], user_id=[9], company_id=[10], event=row[11])
            
            schema_level_object.append(schema_level)
        
        session.add_all(schema_level_object)

        try:

            session.commit()
        
        except Exception as identifier:
        
            logging.error(identifier)
        
        logging.info("Schema level dumped to snowflakes databases.")



