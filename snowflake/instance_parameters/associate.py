import sys

sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')
sys.path.insert(1,  '/snowflake-backend/snowflake/instance_parameters')

from connection import SnowflakeConnector
from record_parameters import RecordParameters

import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)


class AssociateInstance(instance_id):

    def __init__(slef):
        self.instance_id = instance_id

    def associate_instance_to_account_parameters(self):
        pass
    
    def associate_instance_to_databases(self):
        pass

    def associate_instance_to_database_level(self):
        pass
    
    def associate_instance_to_schema(self):
        pass
    
    def associate_instance_to_schema_level(self):
        pass



