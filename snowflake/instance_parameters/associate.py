import sys

sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')
sys.path.insert(1,  '/snowflake-backend/snowflake/instance_parameters')

from connection import SnowflakeConnector
from record_parameters import RecordParameters

import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)


class AssociateInstance():

    def __init__(self, instance_id, account_parameters=None, databases=None, schema=None):
        self.instance_id = instance_id
        self.account_parameters = account_parameters
        self.databases = databases
        self.schema = schema

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

            #append each updated row in the new list.
            results.append(row)

        #finally return associated data as a list.  
        return results

    def associate_instance_to_database_level(self):
        pass
    
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

            #append each updated row in the new list.
            results.append(row)

        #finally return associated data as a list.  
        return results
    
    def associate_instance_to_schema_level(self):
        pass



