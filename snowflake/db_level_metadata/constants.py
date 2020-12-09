# --The roles that can be applied to the current user.
SQL_INFORMATION_SCHEMA_APPLICABLE_ROLES = 'SELECT * FROM {}.INFORMATION_SCHEMA.APPLICABLE_ROLES;' 
TABLE_INFORMATION_SCHEMA_APPLICABLE_ROLES = 'info_schema_applicable_roles'

# --The columns of tables defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_COLUMNS = 'SELECT * FROM {}.INFORMATION_SCHEMA.COLUMNS;' 
TABLE_INFORMATION_SCHEMA_COLUMNS = 'info_schema_columns'

#--The databases that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_DATABASES = 'SELECT * FROM {}.INFORMATION_SCHEMA.DATABASES;' 
TABLE_INFORMATION_SCHEMA_DATABASES = 'info_schema_databases'

#--The roles that are enabled to the current user.
SQL_INFORMATION_SCHEMA_ENABLED_ROLES = 'SELECT * FROM {}.INFORMATION_SCHEMA.ENABLED_ROLES;' 
TABLE_INFORMATION_SCHEMA_ENABLED_ROLES = 'info_schema_enabled_roles'

#--The external tables defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_EXTERNAL_TABLES = 'SELECT * FROM {}.INFORMATION_SCHEMA.EXTERNAL_TABLES;' 
TABLE_INFORMATION_SCHEMA_EXTERNAL_TABLES = 'info_schema_external_tables'

 #--The file formats defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_FILE_FORMATS = 'SELECT * FROM {}.INFORMATION_SCHEMA.FILE_FORMATS;' 
TABLE_INFORMATION_SCHEMA_FILE_FORMATS = 'info_schema_file_formats'

#--The user-defined functions defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_FUNCTIONS = 'SELECT * FROM {}.INFORMATION_SCHEMA.FUNCTIONS;' 
TABLE_INFORMATION_SCHEMA_FUNCTIONS = 'info_schema_functions'

#--"Identifies the database (or catalog. in SQL terminology) that contains the information_schema"
SQL_INFORMATION_SCHEMA_CATALOG_NAME = 'SELECT * FROM {}.INFORMATION_SCHEMA.INFORMATION_SCHEMA_CATALOG_NAME;' 
TABLE_INFORMATION_SCHEMA_CATALOG_NAME = 'info_schema_catlog_name'

#--The loading information of the copy command
SQL_INFORMATION_SCHEMA_LOAD_HISTORY= 'SELECT * FROM {}.INFORMATION_SCHEMA.LOAD_HISTORY;' 
TABLE_INFORMATION_SCHEMA_LOAD_HISTORY = 'info_schema_load_history'

#--The loading information of the copy command
SQL_INFORMATION_SCHEMA_OBJECT_PRIVILEGES= 'SELECT * FROM {}.INFORMATION_SCHEMA.OBJECT_PRIVILEGES;' 
TABLE_INFORMATION_SCHEMA_OBJECT_PRIVILEGES = 'info_schema_object_privileges'

#--The pipes defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_PIPES = 'SELECT * FROM {}.INFORMATION_SCHEMA.PIPES;' 
TABLE_INFORMATION_SCHEMA_PIPES = 'info_schema_pipes'

#--The stored procedures defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_PROCEDURES= 'SELECT * FROM {}.INFORMATION_SCHEMA.PROCEDURES;' 
TABLE_INFORMATION_SCHEMA_PROCEDURES = 'info_schema_procedures'

#--Referential Constraints in this database that are accessible to the current user
SQL_INFORMATION_SCHEMA_REFERENTIAL_CONSTRAINTS= 'SELECT * FROM {}.INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS;' 
TABLE_INFORMATION_SCHEMA_REFERENTIAL_CONSTRAINTS = 'info_schema_referential_constraints'

#--Referential Constraints in this database that are accessible to the current user
SQL_INFORMATION_SCHEMA_REPLICATION_DATABASES= 'SELECT * FROM {}.INFORMATION_SCHEMA.REPLICATION_DATABASES;' 
TABLE_INFORMATION_SCHEMA_REPLICATION_DATABASES = 'info_schema_replication_databases'

#--The schemas defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_SCHEMATA = 'SELECT * FROM {}.INFORMATION_SCHEMA.SCHEMATA;' 
TABLE_INFORMATION_SCHEMA_SCHEMATA = 'info_schema_schemata'

# --The sequences defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_SEQUENCES = 'SELECT * FROM {}.INFORMATION_SCHEMA.SEQUENCES;' 
TABLE_INFORMATION_SCHEMA_SEQUENCES = 'info_schema_sequences'

#--Stages in this database that are accessible by the current user's role
SQL_INFORMATION_SCHEMA_STAGES = 'SELECT * FROM {}.INFORMATION_SCHEMA.STAGES;' 
TABLE_INFORMATION_SCHEMA_STAGES = 'info_schema_stages'

#--The tables defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_TABLES = 'SELECT * FROM {}.INFORMATION_SCHEMA.TABLES;' 
TABLE_INFORMATION_SCHEMA_TABLES = 'info_schema_tables'

#--Constraints defined on the tables in this database that are accessible to the current user
SQL_INFORMATION_SCHEMA_TABLE_CONSTRAINTS = 'SELECT * FROM {}.INFORMATION_SCHEMA.TABLE_CONSTRAINTS;' 
TABLE_INFORMATION_SCHEMA_TABLE_CONSTRAINTS = 'info_schema_tables_constraints'

# --The privileges on tables defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_TABLE_PRIVILEGES = 'SELECT * FROM {}.INFORMATION_SCHEMA.TABLE_PRIVILEGES;' 
TABLE_INFORMATION_SCHEMA_TABLE_PRIVILEGES = 'info_schema_tables_privileges'

#--"All tables within an account. including expired tables."
SQL_INFORMATION_SCHEMA_TABLE_STORAGE_METRICS = 'SELECT * FROM {}.INFORMATION_SCHEMA.TABLE_STORAGE_METRICS;' 
TABLE_INFORMATION_SCHEMA_TABLE_STORAGE_METRICS = 'info_schema_tables_metrics'

#--The usage privileges on sequences defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_USAGE_PRIVILEGES = 'SELECT * FROM {}.INFORMATION_SCHEMA.USAGE_PRIVILEGES;' 
TABLE_INFORMATION_SCHEMA_USAGE_PRIVILEGES = 'info_schema_usage_privileges'

#--The views defined in this database that are accessible to the current user's role.
SQL_INFORMATION_SCHEMA_VIEWS = 'SELECT * FROM {}.INFORMATION_SCHEMA.VIEWS;' 
TABLE_INFORMATION_SCHEMA_VIEWS = 'info_schema_views'