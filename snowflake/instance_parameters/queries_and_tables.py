import sys
sys.path.insert(1,  '/snowflake-backend/snowflake/instance_parameters')
import constants

queries_tables_list = [
    (constants.SQL_ACCOUNT, constants.TABLE_ACCOUNT_PARAMETERS),
    (constants.SQL_DATABASE, constants.TABLE_INSTANCE_PARAMETERS),
    (constants.SQL_DB_LEVEL, constants.TABLE_DB_LEVEL_PARAMETERS),
    (constants.SQL_SCHEMA, constants.TABLE_SCHEMA_PARAMETERS),
    (constants.SQL_SCHEMA_LEVEL, constants.TABLE_SCHEMA_LEVEL_PARAMETERS)
]