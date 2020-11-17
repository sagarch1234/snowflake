import logging
from snowflake.instance_connector.connection import SnowflakeConnector

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)


class RecordParameters():
    '''
    '''
    def __init__(self, connection):
        self.connection = connection

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

        for database in databases:

            result = self.connection.execute('show parameters in DATABASE' + ' ' + database['name']).fetchall()
            
            return result

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

        for database in databases:

            schemas = self.get_schema(database['name'])

            logging.info("Getting parameters in schemas for each database.")

            schema_params = []
            
            for schema in schemas:

                sql = "show parameters in SCHEMA" + " " + database['name'] + "." + schema['name']
 
                schema_params.append(self.connection.execute(sql).fetchall())

        return schema_params


#check and connect to instance
# instance = SnowflakeConnector('jeet', 'Jeet@123', 'fp43891.us-central1.gcp', 'ACCOUNTADMIN')
# connection = instance.connect_snowflake_instance()

# record_parameter = RecordParameters(connection['connection_object'])

# schema_level = record_parameter.schema_level()
# print(schema_level)
