import sys
sys.path.insert(1,  '/snowflake-backend/snowflake/instance_parameters')
import constants

queries_tables_list = [
    (constants.SQL_ACCOUNT_PARAMETERS, constants.TABLE_ACCOUNT_PARAMETERS),
    (constants.SQL_DATABASES, constants.TABLE_DATABASES),
    (constants.SQL_DB_LEVEL_PARAMETERS, constants.TABLE_DB_LEVEL_PARAMETERS),
    (constants.SQL_SCHEMAS, constants.TABLE_SCHEMAS),
    (constants.SQL_SCHEMA_PARAMETERS, constants.TABLE_SCHEMA_PARAMETERS)
]