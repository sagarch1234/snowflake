from sqlalchemy import create_engine
import status
import os
import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)


class SnowflakeConnector():

    def __init__(self, user, password, account, role, database_name=None, schema_name=None, warehouse=None):
        self.user = user
        self.password = password
        self.account = account
        self.role = role
        self.database_name = database_name
        self.schema_name = schema_name
        self.warehouse = warehouse
    
    def get_engine(self):

        logging.info("Create snowflake engine.")

        engine = create_engine('snowflake://{user}:{password}@{account}/{database_name}/{schema_name}?{warehouse}&{role}'.format(user=self.user, password=self.password, account=self.account, role=self.role, database_name=self.database_name, schema_name=self.schema_name, warehouse=self.warehouse), echo=True)        

        return engine

    def connect_snowflake_instance(self):

        engine = self.get_engine()

        try:

            logging.info("Connect to snowflake instance.")
            connection = engine.connect()
        
        except Exception as error_message:

            logging.error(error_message)

            error = {
                "error_message" : "Failed to connect to snowflake instance. Please very your credentials.",
                "status" : status.HTTP_400_BAD_REQUEST
            }

            return error

        logging.info("Connected to snowflake instance.")

        return {
            "connection_object" : connection,
            "engine" : engine,
            "message" : "Connection successful.",
            "status" : status.HTTP_200_OK
        }


class CloseSnowflakeConnection():

    def __init__(self, connection_object):

        self.connection_object = connection_object

    def close_connected_instance(self):

        logging.info("Closing snowflake connection.")
        
        self.connection_object.close()


class DisposeEngine():

    def __init__(self, engine):

        self.engine = engine

    def close_engine(self):

        logging.info("Disposing snowflake engine.")

        self.engine.dispose()