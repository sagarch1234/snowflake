import sys

sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')
sys.path.insert(1,  '/snowflake-backend/snowflake/instance_parameters')

from connection import SnowflakeConnector
from record_parameters import RecordParameters

import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)


class AssociateInstance():

    def __init__(self, instance_id, user_id, company_id, event, account_parameters=None, databases=None, schema=None, database_level=None, schema_level=None):
        self.instance_id = instance_id
        self.account_parameters = account_parameters
        self.databases = databases
        self.schema = schema
        self.user_id = user_id
        self.company_id = company_id
        self.event = event
        self.database_level = database_level
        self.schema_level = schema_level

    def associate_instance_to_account_parameters(self):

        if self.account_parameters is None:

            logging.info("No account parameters found, method will return None")

            return None
        
        #a new list were rows associated with the instance_id will be stored.
        results = []
        
        for row in self.account_parameters:

            row = list(row)

            #associate each row of account_parameters with the instance_id
            row.append(self.instance_id)
            row.append(self.user_id)
            row.append(self.company_id)
            row.append(self.event)

            #append each updated row in the new list.
            results.append(row)

        #finally return associated data as a list.  
        return results
    
    def associate_instance_to_databases(self):

        if self.databases is None:

            logging.info("No databases found, method will return None")

            return None

        #a new list were rows associated with the instance_id will be stored.
        results = []
        
        for row in self.databases:

            row = list(row)

            #associate each row of databases with the instance_id
            row.append(self.instance_id)
            row.append(self.user_id)
            row.append(self.company_id)
            row.append(self.event)

            #append each updated row in the new list.
            results.append(row)

        #finally return associated data as a list.  
        return results

    def associate_instance_to_database_level(self):

        #handle none condition
        if self.database_level is None:

            logging.info("No database_level found.")
            
            return None
        
        results = []
        
        for row in self.database_level:

            row = list(row)

            #associate each row of databases with the instance_id, user_id, company_id, event
            row.append(self.instance_id)
            row.append(self.user_id)
            row.append(self.company_id)
            row.append(self.event)

            #append each updated row in the new list.
            results.append(row)

        return results
    
    def associate_instance_to_schema(self):

        if self.schema is None:

            logging.info("No Schema found, method will return None")

            return None

        #a new list were rows associated with the instance_id will be stored.
        results = []
        
        for row in self.schema:

            row = list(row)

            #associate each row of schema with the instance_id
            row.append(self.instance_id)
            row.append(self.user_id)
            row.append(self.company_id)
            row.append(self.event)

            #append each updated row in the new list.
            results.append(row)

        #finally return associated data as a list.  
        return results
    
    def associate_instance_to_schema_level(self):
        #handle None condition
        if self.schema_level is None:

            logging.info("No schema level parameters found.")

            return None
 
        results = []

        for row in self.schema_level:

            row = list(row)

            row.append(self.instance_id)
            row.append(self.user_id)
            row.append(self.company_id)
            row.append(self.event)

            #append each updated row in the new list.
            results.append(row)

        return results
        
