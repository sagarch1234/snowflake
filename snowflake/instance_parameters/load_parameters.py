import sys

sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')
sys.path.insert(1,  '/snowflake-backend/snowflake/instance_parameters')

from connection import SnowflakeConnector
from record_parameters import RecordParameters

import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)


class DumpParameters():

    def __init__(slef):
        pass

    def dump_account_parameters(self):
        pass
    
    def dump_databases(self):
        pass

    def dump_database_level(self):
        pass
    
    def dump_schema(self):
        pass
    
    def dump_schema_level(self):
        pass



