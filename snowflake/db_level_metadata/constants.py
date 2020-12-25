# --The roles that can be applied to the current user.
SQL_INFORMATION_SCHEMA_APPLICABLE_ROLES = 'SELECT * FROM {}.INFORMATION_SCHEMA.APPLICABLE_ROLES;' 
TABLE_INFORMATION_SCHEMA_APPLICABLE_ROLES = 'info_schema_applicable_roles'
INDEX_INFORMATION_SCHEMA_APPLICABLE_ROLES = 'ID'

# --The columns of tables defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_COLUMNS = 'SELECT * FROM {}.INFORMATION_SCHEMA.COLUMNS;' 
TABLE_INFORMATION_SCHEMA_COLUMNS = 'info_schema_columns'
INDEX_INFORMATION_SCHEMA_COLUMNS = 'ID'

#--The databases that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_DATABASES = 'SELECT * FROM {}.INFORMATION_SCHEMA.DATABASES;' 
TABLE_INFORMATION_SCHEMA_DATABASES = 'info_schema_databases'
INDEX_INFORMATION_SCHEMA_DATABASES = 'ID'

#--The roles that are enabled to the current user.
SQL_INFORMATION_SCHEMA_ENABLED_ROLES = 'SELECT * FROM {}.INFORMATION_SCHEMA.ENABLED_ROLES;' 
TABLE_INFORMATION_SCHEMA_ENABLED_ROLES = 'info_schema_enabled_roles'
INDEX_INFORMATION_SCHEMA_ENABLED_ROLES = 'ID'

#--The external tables defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_EXTERNAL_TABLES = 'SELECT * FROM {}.INFORMATION_SCHEMA.EXTERNAL_TABLES;' 
TABLE_INFORMATION_SCHEMA_EXTERNAL_TABLES = 'info_schema_external_tables'
INDEX_INFORMATION_SCHEMA_EXTERNAL_TABLES = 'ID'

 #--The file formats defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_FILE_FORMATS = 'SELECT * FROM {}.INFORMATION_SCHEMA.FILE_FORMATS;' 
TABLE_INFORMATION_SCHEMA_FILE_FORMATS = 'info_schema_file_formats'
INDEX_INFORMATION_SCHEMA_FILE_FORMATS = 'ID'


#--The user-defined functions defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_FUNCTIONS = 'SELECT * FROM {}.INFORMATION_SCHEMA.FUNCTIONS;' 
TABLE_INFORMATION_SCHEMA_FUNCTIONS = 'info_schema_functions'
INDEX_INFORMATION_SCHEMA_FUNCTIONS = 'ID'

#--"Identifies the database (or catalog. in SQL terminology) that contains the information_schema"
SQL_INFORMATION_SCHEMA_CATALOG_NAME = 'SELECT * FROM {}.INFORMATION_SCHEMA.INFORMATION_SCHEMA_CATALOG_NAME;' 
TABLE_INFORMATION_SCHEMA_CATALOG_NAME = 'info_schema_catlog_name'
INDEX_INFORMATION_SCHEMA_CATALOG_NAME = 'ID'

#--The loading information of the copy command
SQL_INFORMATION_SCHEMA_LOAD_HISTORY= 'SELECT * FROM {}.INFORMATION_SCHEMA.LOAD_HISTORY;' 
TABLE_INFORMATION_SCHEMA_LOAD_HISTORY = 'info_schema_load_history'
INDEX_INFORMATION_SCHEMA_LOAD_HISTORY = 'ID'

#--The loading information of the copy command
SQL_INFORMATION_SCHEMA_OBJECT_PRIVILEGES= 'SELECT * FROM {}.INFORMATION_SCHEMA.OBJECT_PRIVILEGES;' 
TABLE_INFORMATION_SCHEMA_OBJECT_PRIVILEGES = 'info_schema_object_privileges'
INDEX_INFORMATION_SCHEMA_OBJECT_PRIVILEGES = 'ID'

#--The pipes defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_PIPES = 'SELECT * FROM {}.INFORMATION_SCHEMA.PIPES;' 
TABLE_INFORMATION_SCHEMA_PIPES = 'info_schema_pipes'
INDEX_INFORMATION_SCHEMA_PIPES = 'ID'

#--The stored procedures defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_PROCEDURES= 'SELECT * FROM {}.INFORMATION_SCHEMA.PROCEDURES;' 
TABLE_INFORMATION_SCHEMA_PROCEDURES = 'info_schema_procedures'
INDEX_INFORMATION_SCHEMA_PROCEDURES = 'ID'

#--Referential Constraints in this database that are accessible to the current user
SQL_INFORMATION_SCHEMA_REFERENTIAL_CONSTRAINTS= 'SELECT * FROM {}.INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS;' 
TABLE_INFORMATION_SCHEMA_REFERENTIAL_CONSTRAINTS = 'info_schema_referential_constraints'
INDEX_INFORMATION_SCHEMA_REFERENTIAL_CONSTRAINTS = 'ID'

#--Referential Constraints in this database that are accessible to the current user
SQL_INFORMATION_SCHEMA_REPLICATION_DATABASES= 'SELECT * FROM {}.INFORMATION_SCHEMA.REPLICATION_DATABASES;' 
TABLE_INFORMATION_SCHEMA_REPLICATION_DATABASES = 'info_schema_replication_databases'
INDEX_INFORMATION_SCHEMA_REPLICATION_DATABASES = 'ID'

#--The schemas defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_SCHEMATA = 'SELECT * FROM {}.INFORMATION_SCHEMA.SCHEMATA;' 
TABLE_INFORMATION_SCHEMA_SCHEMATA = 'info_schema_schemata'
INDEX_INFORMATION_SCHEMA_SCHEMATA = 'ID'

# --The sequences defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_SEQUENCES = 'SELECT * FROM {}.INFORMATION_SCHEMA.SEQUENCES;' 
TABLE_INFORMATION_SCHEMA_SEQUENCES = 'info_schema_sequences'
INDEX_INFORMATION_SCHEMA_SEQUENCES = 'ID'

#--Stages in this database that are accessible by the current user's role
SQL_INFORMATION_SCHEMA_STAGES = 'SELECT * FROM {}.INFORMATION_SCHEMA.STAGES;' 
TABLE_INFORMATION_SCHEMA_STAGES = 'info_schema_stages'
INDEX_INFORMATION_SCHEMA_STAGES = 'ID'

#--The tables defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_TABLES = 'SELECT * FROM {}.INFORMATION_SCHEMA.TABLES;' 
TABLE_INFORMATION_SCHEMA_TABLES = 'info_schema_tables'
INDEX_INFORMATION_SCHEMA_TABLES = 'ID'

#--Constraints defined on the tables in this database that are accessible to the current user
SQL_INFORMATION_SCHEMA_TABLE_CONSTRAINTS = 'SELECT * FROM {}.INFORMATION_SCHEMA.TABLE_CONSTRAINTS;' 
TABLE_INFORMATION_SCHEMA_TABLE_CONSTRAINTS = 'info_schema_tables_constraints'
INDEX_INFORMATION_SCHEMA_TABLE_CONSTRAINTS = 'ID'

# --The privileges on tables defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_TABLE_PRIVILEGES = 'SELECT * FROM {}.INFORMATION_SCHEMA.TABLE_PRIVILEGES;' 
TABLE_INFORMATION_SCHEMA_TABLE_PRIVILEGES = 'info_schema_tables_privileges'
INDEX_INFORMATION_SCHEMA_TABLE_PRIVILEGES = 'ID'

#--"All tables within an account. including expired tables."
SQL_INFORMATION_SCHEMA_TABLE_STORAGE_METRICS = 'SELECT * FROM {}.INFORMATION_SCHEMA.TABLE_STORAGE_METRICS;' 
TABLE_INFORMATION_SCHEMA_TABLE_STORAGE_METRICS = 'info_schema_tables_metrics'
INDEX_INFORMATION_SCHEMA_TABLE_STORAGE_METRICS = 'ID_TABLE_METRICS'

#--The usage privileges on sequences defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_USAGE_PRIVILEGES = 'SELECT * FROM {}.INFORMATION_SCHEMA.USAGE_PRIVILEGES;' 
TABLE_INFORMATION_SCHEMA_USAGE_PRIVILEGES = 'info_schema_usage_privileges'
INDEX_INFORMATION_SCHEMA_USAGE_PRIVILEGES = 'ID'

#--The views defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_VIEWS = 'SELECT * FROM {}.INFORMATION_SCHEMA.VIEWS;' 
TABLE_INFORMATION_SCHEMA_VIEWS = 'info_schema_views'
INDEX_INFORMATION_SCHEMA_VIEWS = 'ID'