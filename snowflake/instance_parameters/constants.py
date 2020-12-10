#account level
SQL_ACCOUNT = 'SHOW PARAMETERS IN ACCOUNT;'
TABLE_ACCOUNT_PARAMETERS = 'account_parameters'

#database
SQL_DATABASE = 'SHOW DATABASES;'
TABLE_DATABASE_PARAMETERS = 'instance_databases'

#db level
SQL_DB_LEVEL = "SHOW PARAMETERS IN DATABASE {};"
TABLE_DB_LEVEL_PARAMETERS = 'parameters_in_database'

#schema
SQL_SCHEMA = 'SHOW SCHEMAS;'
TABLE_SCHEMA_PARAMETERS = 'instance_databases_schema'

#schema level
SQL_SCHEMA_LEVEL = "SHOW PARAMETERS IN SCHEMA {}.{};"
TABLE_SCHEMA_LEVEL_PARAMETERS = 'parameters_in_schemas'