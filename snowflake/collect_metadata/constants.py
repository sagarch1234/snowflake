
#clustering history
SQL_ACCOUNT_USAGE_AUTOMATIC_CLUSTERING_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.AUTOMATIC_CLUSTERING_HISTORY;'
TABLE_ACCOUNT_USAGE_AUTOMATIC_CLUSTERING_HISTORY = 'account_usage_automatic_clustering_history'
INDEX_ACCOUNT_USAGE_AUTOMATIC_CLUSTERING_HISTORY = 'ID'

#account ussage columns
SQL_ACCOUNT_USAGE_COLUMNS = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.COLUMNS;'
TABLE_ACCOUNT_USAGE_COLUMNS = 'account_usage_columns'
INDEX_ACCOUNT_USAGE_COLUMNS = 'ID'

# --HANGS
#copy account usage history
SQL_ACCOUNT_USAGE_COPY_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.COPY_HISTORY;'
TABLE_ACCOUNT_USAGE_COPY_HISTORY = 'account_usage_copy_history'
INDEX_ACCOUNT_USAGE_COPY_HISTORY = 'ID'

#account usage history
SQL_ACCOUNT_USAGE_DATABASES = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASES;'
TABLE_ACCOUNT_USAGE_DATABASES = 'account_usage_databases'
INDEX_ACCOUNT_USAGE_DATABASES = 'ID'

#--NOT BEING POPULATED
#databases storage usage history
SQL_ACCOUNT_USAGE_DATABASE_STORAGE_USAGE_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASE_STORAGE_USAGE_HISTORY; '
TABLE_ACCOUNT_USAGE_DATABASE_STORAGE_USAGE_HISTORY = 'account_usage_database_storage_usage_history'
INDEX_ACCOUNT_USAGE_DATABASE_STORAGE_USAGE_HISTORY = 'ID'

#data transfer history
SQL_ACCOUNT_USAGE_DATA_TRANSFER_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.DATA_TRANSFER_HISTORY;'
TABLE_ACCOUNT_USAGE_DATA_TRANSFER_HISTORY = 'account_usage_data_transfer_history'
INDEX_ACCOUNT_USAGE_DATA_TRANSFER_HISTORY = 'ID'

#file formats
SQL_ACCOUNT_USAGE_FILE_FORMATS = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.FILE_FORMATS;'
TABLE_ACCOUNT_USAGE_FILE_FORMATS = 'account_usage_file_formats'
INDEX_ACCOUNT_USAGE_FILE_FORMATS = 'ID'

#functions
SQL_ACCOUNT_USAGE_FUNCTIONS = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.FUNCTIONS;'
TABLE_ACCOUNT_USAGE_FUNCTIONS = 'account_usage_functions'
INDEX_ACCOUNT_USAGE_FUNCTIONS = 'ID'

#grants to roles
SQL_ACCOUNT_USAGE_GRANTS_TO_ROLES = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.GRANTS_TO_ROLES;'
TABLE_ACCOUNT_USAGE_GRANTS_TO_ROLES = 'account_usage_grants_to_roles'
INDEX_ACCOUNT_USAGE_GRANTS_TO_ROLES = 'ID'

#grants to users
SQL_ACCOUNT_USAGE_GRANTS_TO_USERS = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.GRANTS_TO_USERS;'
TABLE_ACCOUNT_USAGE_GRANTS_TO_USERS = 'account_usage_grants_to_users'
INDEX_ACCOUNT_USAGE_GRANTS_TO_USERS = 'ID'

#load history
SQL_ACCOUNT_USAGE_LOAD_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.LOAD_HISTORY;'
TABLE_ACCOUNT_USAGE_LOAD_HISTORY = 'account_usage_load_history'
INDEX_ACCOUNT_USAGE_LOAD_HISTORY = 'ID'

#login history
SQL_ACCOUNT_USAGE_LOGIN_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.LOGIN_HISTORY;'
TABLE_ACCOUNT_USAGE_LOGIN_HISTORY = 'account_usage_login_history'
INDEX_ACCOUNT_USAGE_LOGIN_HISTORY = 'ID'

#materialized view refresh history
SQL_ACCOUNT_USAGE_MATERIALIZED_VIEW_REFRESH_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.MATERIALIZED_VIEW_REFRESH_HISTORY;'
TABLE_ACCOUNT_USAGE_MATERIALIZED_VIEW_REFRESH_HISTORY  = 'account_usage_materialized_view_refresh_history'
INDEX_ACCOUNT_USAGE_MATERIALIZED_VIEW_REFRESH_HISTORY = 'ID'

# -- Credits used by date.
#metering daily history
SQL_ACCOUNT_USAGE_METERING_DAILY_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.METERING_DAILY_HISTORY;'
TABLE_ACCOUNT_USAGE_METERING_DAILY_HISTORY  = 'account_usage_metering_daily_history'
INDEX_ACCOUNT_USAGE_METERING_DAILY_HISTORY = 'ID'

#-- Compute used including Cloud Services
#metering history
SQL_ACCOUNT_USAGE_METERING_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.METERING_HISTORY; '
TABLE_ACCOUNT_USAGE_METERING_HISTORY  = 'account_usage_metering_history'
INDEX_ACCOUNT_USAGE_METERING_HISTORY = 'ID'

#pipes
SQL_ACCOUNT_USAGE_PIPES = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.PIPES;'
TABLE_ACCOUNT_USAGE_PIPES= 'account_usage_pipes'
INDEX_ACCOUNT_USAGE_PIPES = 'ID'

#pipe usage history
SQL_ACCOUNT_USAGE_PIPE_USAGE_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.PIPE_USAGE_HISTORY;'
TABLE_ACCOUNT_USAGE_PIPE_USAGE_HISTORY = 'account_usage_pipe_usage_history'
INDEX_ACCOUNT_USAGE_PIPE_USAGE_HISTORY = 'ID'

#-- Important
#query history
SQL_ACCOUNT_USAGE_QUERY_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY;'
TABLE_ACCOUNT_USAGE_QUERY_HISTORY = 'account_usage_query_history'
INDEX_ACCOUNT_USAGE_QUERY_HISTORY = 'ID'

#referential constraints
SQL_ACCOUNT_USAGE_REFERENTIAL_CONSTRAINTS = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.REFERENTIAL_CONSTRAINTS;'
TABLE_ACCOUNT_USAGE_REFERENTIAL_CONSTRAINTS = 'acccount_usage_referential_constraints'
INDEX_ACCOUNT_USAGE_REFERENTIAL_CONSTRAINTS = 'ID'

#replication usage history
SQL_ACCOUNT_USAGE_REPLICATION_USAGE_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.REPLICATION_USAGE_HISTORY;'
TABLE_ACCOUNT_USAGE_REPLICATION_USAGE_HISTORY = 'acccount_usage_replication_usage_history'
INDEX_ACCOUNT_USAGE_REPLICATION_USAGE_HISTORY = 'ID'

#roles
SQL_ACCOUNT_USAGE_ROLES = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.ROLES;'
TABLE_ACCOUNT_USAGE_ROLES = 'acccount_usage_role'
INDEX_ACCOUNT_USAGE_ROLES = 'ID'

#schemata
SQL_ACCOUNT_USAGE_SCHEMATA = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.SCHEMATA;'
TABLE_ACCOUNT_USAGE_SCHEMATA = 'acccount_usage_schemata'
INDEX_ACCOUNT_USAGE_SCHEMATA = 'ID'

#search optimization history
#--opt
SQL_ACCOUNT_USAGE_SEARCH_OPTIMIZATION_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.SEARCH_OPTIMIZATION_HISTORY;'
TABLE_ACCOUNT_USAGE_SEARCH_OPTIMIZATION_HISTORY = 'acccount_usage_search_optimization_history'
INDEX_ACCOUNT_USAGE_SEARCH_OPTIMIZATION_HISTORY = 'ID'

# --opt
#sequences
SQL_ACCOUNT_USAGE_SEQUENCES = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.SEQUENCES;'
TABLE_ACCOUNT_USAGE_SEQUENCES = 'acccount_usage_sequences'
INDEX_ACCOUNT_USAGE_SEQUENCES = 'ID'

#--opt
#stages
SQL_ACCOUNT_USAGE_STAGES = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.STAGES;'
TABLE_ACCOUNT_USAGE_STAGES = 'acccount_usage_stages'
INDEX_ACCOUNT_USAGE_STAGES = 'ID'

# --opt
#stage storage usage history
SQL_ACCOUNT_USAGE_STAGE_STORAGE_USAGE_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.STAGE_STORAGE_USAGE_HISTORY;'
TABLE_ACCOUNT_USAGE_STAGE_STORAGE_USAGE_HISTORY = 'acccount_usage_stage_storage_usage_history'
INDEX_ACCOUNT_USAGE_STAGE_STORAGE_USAGE_HISTORY = 'ID'

#--opt
#storage usage
SQL_ACCOUNT_USAGE_STORAGE_USAGE = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.STORAGE_USAGE;'
TABLE_ACCOUNT_USAGE_STORAGE_USAGE = 'acccount_usage_storage_usage'
INDEX_ACCOUNT_USAGE_STORAGE_USAGE = 'ID'

#tables
SQL_ACCOUNT_USAGE_TABLES = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.TABLES;'
TABLE_ACCOUNT_USAGE_TABLES = 'acccount_usage_tables'
INDEX_ACCOUNT_USAGE_TABLES = 'ID'

#constraints
SQL_ACCOUNT_USAGE_TABLE_CONSTRAINTS = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.TABLE_CONSTRAINTS;'
TABLE_ACCOUNT_USAGE_TABLE_CONSTRAINTS = 'acccount_usage_table_constraints'
INDEX_ACCOUNT_USAGE_TABLE_CONSTRAINTS = 'ID'

#table storage metrics
# --opt
SQL_ACCOUNT_USAGE_TABLE_STORAGE_METRICS = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.TABLE_STORAGE_METRICS;'
TABLE_ACCOUNT_USAGE_TABLE_STORAGE_METRICS = 'acccount_usage_storage_metrics'
INDEX_ACCOUNT_USAGE_TABLE_STORAGE_METRICS = 'STORAGE_METRIC_ID'

#users
# --opt
SQL_ACCOUNT_USAGE_USERS = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.USERS;'
TABLE_ACCOUNT_USAGE_USERS = 'acccount_usage_users'
INDEX_ACCOUNT_USAGE_USERS = 'ID'

#views
# --opt
SQL_ACCOUNT_USAGE_VIEWS = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.VIEWS;'
TABLE_ACCOUNT_USAGE_VIEWS = 'acccount_usage_views'
INDEX_ACCOUNT_USAGE_VIEWS = 'ID'

#warehouse load history
#--opt
SQL_ACCOUNT_USAGE_WAREHOUSE_LOAD_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_LOAD_HISTORY;' 
TABLE_ACCOUNT_USAGE_WAREHOUSE_LOAD_HISTORY = 'acccount_usage_warehouse_load_history'
INDEX_ACCOUNT_USAGE_WAREHOUSE_LOAD_HISTORY = 'ID'

#warehouse metering history
# --opt
SQL_ACCOUNT_USAGE_WAREHOUSE_METERING_HISTORY = 'SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY;'
TABLE_ACCOUNT_USAGE_WAREHOUSE_METERING_HISTORY = 'acccount_usage_warehouse_metering_history'
INDEX_ACCOUNT_USAGE_WAREHOUSE_METERING_HISTORY = 'ID'

#preview data transfer daily history
SQL_ORGANIZATION_USAGE_PREVIEW_DATA_TRANSFER_DAILY_HISTORY = 'SELECT * FROM SNOWFLAKE.ORGANIZATION_USAGE.PREVIEW_DATA_TRANSFER_DAILY_HISTORY;'
TABLE_ORGANIZATION_USAGE_PREVIEW_DATA_TRANSFER_DAILY_HISTORY = 'organization_usage_preview_data_transfer_daily_history'
INDEX_ORGANIZATION_USAGE_PREVIEW_DATA_TRANSFER_DAILY_HISTORY = 'ID'

#preview metering transfer daily history
SQL_ORGANIZATION_USAGE_PREVIEW_METERING_DAILY_HISTORY = 'SELECT * FROM SNOWFLAKE.ORGANIZATION_USAGE.PREVIEW_METERING_DAILY_HISTORY;'
TABLE_ORGANIZATION_USAGE_PREVIEW_METERING_DAILY_HISTORY = 'organization_usage_preview_metering_daily_history'
INDEX_ORGANIZATION_USAGE_PREVIEW_METERING_DAILY_HISTORY = 'ID'

#preview storage daily history
SQL_ORGANIZATION_USAGE_PREVIEW_STORAGE_DAILY_HISTORY = 'SELECT * FROM SNOWFLAKE.ORGANIZATION_USAGE.PREVIEW_STORAGE_DAILY_HISTORY;'
TABLE_ORGANIZATION_USAGE_PREVIEW_STORAGE_DAILY_HISTORY = 'organization_usage_preview_storage_daily_history'
INDEX_ORGANIZATION_USAGE_PREVIEW_STORAGE_DAILY_HISTORY = 'ID'

#login history
SQL_READER_ACCOUNT_USAGE_LOGIN_HISTORY = 'SELECT * FROM SNOWFLAKE.READER_ACCOUNT_USAGE.LOGIN_HISTORY;'
TABLE_READER_ACCOUNT_USAGE_LOGIN_HISTORY = 'reader_account_usage_login_history'
INDEX_READER_ACCOUNT_USAGE_LOGIN_HISTORY = 'ID'

#query history
SQL_READER_ACCOUNT_USAGE_QUERY_HISTORY = 'SELECT * FROM SNOWFLAKE.READER_ACCOUNT_USAGE.QUERY_HISTORY;'
TABLE_READER_ACCOUNT_USAGE_QUERY_HISTORY = 'reader_account_usage_query_history'
INDEX_READER_ACCOUNT_USAGE_QUERY_HISTORY = 'ID'

#resource monitors
SQL_READER_ACCOUNT_USAGE_RESOURCE_MONITORS = 'SELECT * FROM SNOWFLAKE.READER_ACCOUNT_USAGE.RESOURCE_MONITORS;'
TABLE_READER_ACCOUNT_USAGE_RESOURCE_MONITORS = 'reader_account_usage_resource_monitor'
INDEX_READER_ACCOUNT_USAGE_RESOURCE_MONITORS = 'ID'

#storage usage
SQL_READER_ACCOUNT_USAGE_STORAGE_USAGE = 'SELECT * FROM SNOWFLAKE.READER_ACCOUNT_USAGE.STORAGE_USAGE;'
TABLE_READER_ACCOUNT_USAGE_STORAGE_USAGE = 'reader_account_usage_storage_usage'
INDEX_READER_ACCOUNT_USAGE_STORAGE_USAGE = 'ID'

#warehouse metering history
SQL_READER_ACCOUNT_USAGE_WAREHOUSE_METERING_HISTORY = 'SELECT * FROM SNOWFLAKE.READER_ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY;'
TABLE_READER_ACCOUNT_USAGE_WAREHOUSE_METERING_HISTORY = 'reader_account_usage_warehouse_metering_history'
INDEX_READER_ACCOUNT_USAGE_WAREHOUSE_METERING_HISTORY = 'ID'