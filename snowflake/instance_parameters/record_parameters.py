import sys
import logging
import json
import os

sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')
sys.path.insert(1,  '/snowflake-backend/snowflake/instance_parameters')

from connection import SnowflakeConnector


logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)

class RecordParameters():
    '''
    '''
    def __init__(self, connection, instance_id=None):
        self.connection = connection
        self.instance_id = instance_id

    def account_level(self):

        logging.info("Collecting account's parameters from customer's instance.")

        results = self.connection.execute('show parameters in account').fetchall()

        return results

    def get_databases(self):

        logging.info("Geting list of databases form customer's instance.")

        results = self.connection.execute('show databases').fetchall()

        return results

    def database_level(self):

        logging.info("Getting parameters of each database.")

        databases = self.get_databases()

        if databases is None:
            return None

        databases_level = []
        
        for database in databases:

            result = self.connection.execute('show parameters in DATABASE' + ' ' + database['name']).fetchall()

            for row in result:

                row = list(row)

                row.append(database['name'])

                databases_level.append(row)

        return databases_level

    def get_schema(self, database_name=None):

        logging.info("Get databases.")
        
        if database_name == None:

            logging.info("Getting schemas of instances.")

            sql = 'show schemas'

        else:

            logging.info("Getting schemas for database " +"'"+ database_name +"'.")
        
            sql = 'show schemas in database' + ' ' + database_name

        results = self.connection.execute(sql).fetchall()

        return results

    def schema_level(self):
        
        logging.info("Get databases")

        databases = self.get_databases()
        
        results = []

        for database in databases:

            logging.info("Getting parameters in schemas for each database.")

            schemas = self.get_schema(database['name'])

            
            for schema in schemas:

                sql = "show parameters in SCHEMA" + " " + database['name'] + "." + schema['name']
                
                result = self.connection.execute(sql).fetchall()
                
                for row in result:

                    row = list(row)
                    row.append(database['name'])
                    row.append(schema['name'])
                    results.append(row)
                
        return results
