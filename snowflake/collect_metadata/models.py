import sys
import datetime
import os

sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')

from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column, Text, Boolean, create_engine, Time, String, Sequence, DateTime, TIMESTAMP, Date, Float
from snowflake.sqlalchemy import URL, VARIANT

from connection import SnowflakeConnector
from connection import DisposeEngine
import constants


#using declarative base
Base = declarative_base()

#get SnowflakeConnector class object
# connector = SnowflakeConnector(user=os.environ.get('SNOWFLAKE_ACCOUNT_USER'), password=os.environ.get('SNOWFLAKE_ACCOUNT_PASSWORD'), account=os.environ.get('SNOWFLAKE_ACCOUNT'), database_name=os.environ.get('SNOWFLAKE_DATABASE_NAME'), schema_name=os.environ.get('SCHEMA_NAME'), role=os.environ.get('ACCOUNT_ROLE'), warehouse=os.environ.get('ACCOUNT_WAREHOUSE'))

#get engine
# engine = connector.get_engine()


class AccountUsageLoginHistory(Base):
    
    '''
    This model will store the account parameters of the customers instances.
    '''

    __tablename__ = constants.TABLE_ACCOUNT_USAGE_LOGIN_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_account_usage_login_history'), primary_key=True, autoincrement=True)
    event_id = Column(Integer, nullable=True)
    event_timestamp = Column(TIMESTAMP, nullable=True)
    event_type = Column(String(100), nullable=True)
    user_name = Column(String(100), nullable=True)
    client_ip = Column(String(100), nullable=True)
    reported_client_type = Column(String(100), nullable=True)
    reported_client_version = Column(String(100), nullable=True)
    first_authentication_factor = Column(String(100), nullable=True)
    second_authentication_factor = Column(String(100), nullable=True)
    is_success = Column(String(100), nullable=True)
    error_code = Column(String(200), nullable=True) 
    error_message = Column(String(100), nullable=True)
    related_event_id = Column(Integer, nullable=True)
    event = Column(String(200), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<LoginHistory({})>".format(self.id)


class AccountUsageAutomaticClusteringHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_AUTOMATIC_CLUSTERING_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_account_usage_automatic_clustering_history'), primary_key=True, autoincrement=True)
    start_time = Column(TIMESTAMP, nullable=True)
    end_time = Column(TIMESTAMP, nullable=True)
    credit_used = Column(Integer, nullable=True)
    num_bytes_reclustered = Column(Integer, nullable=True)
    num_rows_reclustered = Column(Integer, nullable=True)
    table_id = Column(Integer, nullable=True)
    table_name = Column(String(100), nullable=True)
    schema_id = Column(Integer, nullable=True)
    schema_name = Column(String(100), nullable=True)
    database_id = Column(Integer, nullable=True)
    database_name = Column(String(100), nullable=True)
    event = Column(String(200), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<AUTOMATICCLUSTERINGHISTORY({})>".format(self.id)


class AccountUsageColumns(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_COLUMNS
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_account_usage_columns'), primary_key=True, autoincrement=True)
    column_id = Column(Integer, nullable=True)
    column_name = Column(Text, nullable=True)
    table_id = Column(Integer, nullable=True)
    table_name = Column(Text, nullable=True)
    table_schema_id = Column(Integer, nullable=True)
    table_schema = Column(Text, nullable=True)
    table_catalog_id = Column(Integer, nullable=True)
    table_catalog = Column(Text, nullable=True)
    ordinal_position = Column(Integer, nullable=True)
    column_default = Column(Text, nullable=True)
    is_nullable = Column(Text, nullable=True)
    data_type = Column(Text, nullable=True)
    character_maximum_length = Column(Integer, nullable=True)
    character_octet_length = Column(Integer, nullable=True)
    numeric_precision = Column(Integer, nullable=True)
    numeric_precision_radix = Column(Integer, nullable=True)
    numeric_scale = Column(Integer, nullable=True)
    datetime_precision = Column(Integer, nullable=True)
    interval_type = Column(Text, nullable=True)
    interval_precision = Column(Text, nullable=True)
    character_set_catalog = Column(Text, nullable=True)
    character_set_schema = Column(Text, nullable=True)
    character_set_name = Column(Text, nullable=True)
    collation_catalog = Column(Text, nullable=True)
    collation_schema = Column(Text, nullable=True)
    collation_name = Column(Text, nullable=True)
    domain_catalog = Column(Text, nullable=True)
    domain_schema = Column(Text, nullable=True)
    domain_name = Column(Text, nullable=True)
    udt_catalog = Column(Text, nullable=True)
    udt_schema = Column(Text, nullable=True)
    udt_name = Column(Text, nullable=True)
    scope_catalog = Column(Text, nullable=True)
    scope_schema = Column(Text, nullable=True)
    scope_name = Column(Text, nullable=True)
    maximum_cardinality = Column(Text, nullable=True)
    dtd_identifier = Column(Text, nullable=True)
    is_self_referencing = Column(Text, nullable=True)
    is_identity = Column(Text, nullable=True)
    identity_generation = Column(Text, nullable=True)
    identity_start = Column(Text, nullable=True)
    identity_increment = Column(Text, nullable=True)
    identity_maximum = Column(Text, nullable=True)
    identity_minimum = Column(Text, nullable=True)
    identity_cycle = Column(Text, nullable=True)
    comment = Column(Text, nullable=True)
    deleted = Column(TIMESTAMP, nullable=True)
    event = Column(String(200), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGECOLUMNS({})>".format(self.id)


class AccountUsageCopyHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_COPY_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_account_usage_copy_history'), primary_key=True, autoincrement=True)
    file_name = Column(Text, nullable=True)
    stage_location = Column(Text, nullable=True)
    last_load_time = Column(TIMESTAMP, nullable=True)
    row_count = Column(Integer, nullable=True)
    row_parsed = Column(Integer, nullable=True)
    file_size = Column(Integer, nullable=True)
    first_error_message = Column(Text, nullable=True)
    first_error_line_number = Column(Integer, nullable=True)
    first_error_character_pos = Column(Integer, nullable=True)
    first_error_column_name = Column(Text, nullable=True)
    error_count = Column(Integer, nullable=True)
    error_limit = Column(Integer, nullable=True)
    status = Column(Text, nullable=True)
    table_id = Column(Integer, nullable=True)
    table_name = Column(Text, nullable=True)
    table_schema_id = Column(Integer, nullable=True)
    table_schema_name = Column(Text, nullable=True)
    table_catalog_id = Column(Integer, nullable=True)
    table_catalog_name = Column(Text, nullable=True)
    pipe_catalog_name = Column(Text, nullable=True)
    pipe_schema_name = Column(Text, nullable=True)
    pipe_name = Column(Text, nullable=True)
    pipe_received_time = Column(TIMESTAMP, nullable=True)
    event = Column(String(200), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGECOPYHISTORY({})>".format(self.id)


class AccountUsageDatabases(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_DATABASES
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_account_usage_databases'), primary_key=True, autoincrement=True)
    database_id = Column(Integer, nullable=True) 
    database_name = Column(Text, nullable=True)
    database_owner = Column(Text, nullable=True)
    is_transient = Column(Text, nullable=True)
    comment = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    deleted = Column(TIMESTAMP, nullable=True)
    retention_time = Column(Integer, nullable=True)
    event = Column(String(200), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEDATABASES({})>".format(self.id)


class AccountUsageDatabaseStorageUsageHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_DATABASE_STORAGE_USAGE_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_account_usage_database_storage_usage_history'), primary_key=True, autoincrement=True)
    usage_date = Column(Date, nullable=True)
    database_id = Column(Integer, nullable=True)
    database_name = Column(Text, nullable=True)
    deleted = Column(TIMESTAMP, nullable=True)
    average_database_bytes = Column(Float, nullable=True)
    average_failsafe_bytes = Column(Float, nullable=True)
    event = Column(String(200), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<DATABASESTORAGEUSAGEHISTORY({})>".format(self.id)


class AccountUsageDataTransferHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_DATA_TRANSFER_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }
    id = Column(Integer, Sequence('id_account_usage_data_transfer_history'), primary_key=True, autoincrement=True)
    start_time = Column(TIMESTAMP, nullable=True)
    end_time = Column(TIMESTAMP, nullable=True)
    source_cloud = Column(String(200), nullable=True)
    source_region = Column(String(200), nullable=True)
    target_cloud = Column(String(200), nullable=True)
    target_region = Column(String(200), nullable=True)
    bytes_transferred = Column(Float, nullable=True)
    transfer_type = Column(String(200), nullable=True)
    event = Column(String(200), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<DATATRANSFERHISTORY({})>".format(self.id)


class AccountUsageFileFormats(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_FILE_FORMATS
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }
    id = Column(Integer, Sequence('id_account_usage_file_formats'), primary_key=True, autoincrement=True)
    file_format_id = Column(Integer, nullable=True)
    file_format_name = Column(Text, nullable=True)
    file_format_schema_id = Column(Integer, nullable=True)
    file_format_schema = Column(Text, nullable=True)
    file_format_catalog_id = Column(Integer, nullable=True)
    file_format_catalog = Column(Text, nullable=True)
    file_format_owner = Column(Text, nullable=True)
    file_format_type = Column(Text, nullable=True)
    record_delimiter = Column(Text, nullable=True)
    field_delimiter = Column(Text, nullable=True)
    skip_header = Column(Integer, nullable=True)
    date_format = Column(Text, nullable=True)
    time_format = Column(Text, nullable=True)
    timestamp_format = Column(Text, nullable=True)
    binary_format = Column(Text, nullable=True)
    escape = Column(Text, nullable=True)
    escape_unenclosed_field =Column(Text, nullable=True)
    trim_space = Column(Boolean, nullable=True)
    field_optionally_enclosed_by = Column(Text, nullable=True)
    null_if = Column(Text, nullable=True)
    compression = Column(Text, nullable=True)
    error_on_column_count_mismatch = Column(Boolean, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    deleted = Column(TIMESTAMP, nullable=True)
    comment = Column(Text, nullable=True)
    event = Column(String(200), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<FILEFORMATS({})>".format(self.id)


class AccountUsageFunctions(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_FUNCTIONS
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }
    id = Column(Integer, Sequence('id_account_usage_functions'), primary_key=True, autoincrement=True)
    function_id = Column(Integer, nullable=True)
    function_name = Column(Text, nullable=True)
    function_schema_id = Column(Integer, nullable=True)
    function_schema = Column(Text, nullable=True)
    function_catalog_id = Column(Integer, nullable=True)
    function_catalog = Column(Text, nullable=True)
    function_owner = Column(Text, nullable=True)
    argument_signature = Column(Text, nullable=True)
    data_type = Column(Text, nullable=True)
    character_maximum_length = Column(Integer, nullable=True)
    character_octet_length = Column(Integer, nullable=True)
    numeric_precision = Column(Integer, nullable=True)
    numeric_precision_radix = Column(Integer, nullable=True)
    numeric_scale = Column(Integer, nullable=True)
    function_language = Column(Text, nullable=True)
    function_definition = Column(Text, nullable=True)
    volatility = Column(Text, nullable=True)
    is_null_call = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    deleted = Column(TIMESTAMP, nullable=True)
    comment = Column(Text, nullable=True)
    is_external = Column(String(3), nullable=True)
    api_integration = Column(Text, nullable=True)
    context_headers = Column(Text, nullable=True)
    max_batch_rows = Column(Integer, nullable=True)
    compression = Column(Text, nullable=True)
    event = Column(String(200), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEFUNCTIONS({})>".format(self.id)


class AccountUsageGrantsToRoles(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_GRANTS_TO_ROLES
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }
    id = Column(Integer, Sequence('id_account_usage_grants_to_roles'), primary_key=True, autoincrement=True)
    created_on = Column(TIMESTAMP, nullable=True)
    modified_on = Column(TIMESTAMP, nullable=True)
    privilege = Column(Text, nullable=True)
    granted_on = Column(Text, nullable=True)
    name = Column(Text, nullable=True)
    table_catalog = Column(Text, nullable=True)
    table_schema = Column(Text, nullable=True)
    granted_to = Column(String(4), nullable=True)
    grantee_name = Column(Text, nullable=True)
    grant_option = Column(Boolean, nullable=True)
    granted_by = Column(Text, nullable=True)
    deleted_on = Column(TIMESTAMP, nullable=True)
    event = Column(String(200), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEGRANTSTOROLES({})>".format(self.id)


class AccountUsageGrantsToUsers(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_GRANTS_TO_USERS
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_account_usage_grants_to_users'), primary_key=True, autoincrement=True)
    created_on = Column(TIMESTAMP, nullable=True)
    deleted_on = Column(TIMESTAMP, nullable=True)
    role = Column(Text, nullable=True)
    granted_to = Column(String(4), nullable=True)
    grantee_name = Column(Text, nullable=True)
    granted_by = Column(Text, nullable=True)
    event = Column(String(200), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEGRANTSTOUSERS({})>".format(self.id)


class AccountUsageLoadHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_LOAD_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_account_usage_load_history'), primary_key=True, autoincrement=True)
    table_id = Column(Integer, nullable=True)
    table_name = Column(Text, nullable=True)
    schema_id = Column(Integer, nullable=True)
    schema_name = Column(Text, nullable=True)
    catalog_id = Column(Integer, nullable=True)
    catalog_name = Column(Text, nullable=True)
    file_name = Column(Text, nullable=True)
    last_load_time = Column(TIMESTAMP, nullable=True)
    status = Column(Text, nullable=True)
    row_count = Column(Integer, nullable=True)
    row_parsed = Column(Integer, nullable=True)
    first_error_message = Column(Text, nullable=True)
    first_error_line_number = Column(Integer, nullable=True)
    first_error_character_position = Column(Integer, nullable=True)
    first_error_col_name = Column(Text, nullable=True)
    error_count = Column(Integer, nullable=True)
    error_limit = Column(Integer, nullable=True)
    event = Column(String(200), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGELOADHISTORY({})>".format(self.id)


class AccountUsageMaterializedViewRefreshHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_MATERIALIZED_VIEW_REFRESH_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_account_usage_materialized_view_refresh_history'), primary_key=True, autoincrement=True)
    start_time = Column(TIMESTAMP, nullable=True)
    end_time = Column(TIMESTAMP, nullable=True)
    credits_used = Column(Integer, nullable=True)
    table_id = Column(Integer, nullable=True)
    table_name = Column(Text, nullable=True)
    schema_id = Column(Integer, nullable=True)
    schema_name = Column(Text, nullable=True)
    database_id = Column(Integer, nullable=True)
    database_name = Column(Text, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEMATERIALIZEDVIEWREFRESHHISTORY({})>".format(self.id)


class AccountUsageMeteringDailyHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_METERING_DAILY_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_account_usage_metering_daily_history'), primary_key=True, autoincrement=True)
    service_type = Column(String(25), nullable=True)
    usage_date = Column(Date, nullable=True)
    credits_used_compute = Column(Integer, nullable=True)
    credits_used_cloud_services = Column(Integer, nullable=True)
    credits_used = Column(Integer, nullable=True)
    credits_adjustment_cloud_services = Column(Integer, nullable=True)
    credits_billed = Column(Integer, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEMETERINGDAILYHISTORY({})>".format(self.id)


class AccountUsageMeteringHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_METERING_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_account_usage_metering_history'), primary_key=True, autoincrement=True)
    service_type = Column(String(25), nullable=True)
    start_time = Column(TIMESTAMP, nullable=True)
    end_time = Column(TIMESTAMP, nullable=True)
    entity_id = Column(Integer, nullable=True)
    name = Column(Text, nullable=True)
    credits_used_compute = Column(Integer, nullable=True)
    credits_used_cloud_services = Column(Integer, nullable=True)
    credits_used = Column(Integer, nullable=True)
    bytes  = Column(Float, nullable=True)
    rows = Column("ROWS", Integer, nullable=True)
    files  = Column(Float, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEMETERINGHISTORY({})>".format(self.id)


class AccountUsagePipes(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_PIPES
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_account_usage_pipes'), primary_key=True, autoincrement=True)
    pipe_id = Column(Integer, nullable=True)
    pipe_name = Column(Text, nullable=True)
    pipe_schema_id = Column(Integer, nullable=True)
    pipe_schema = Column(Text, nullable=True)
    pipe_catalog_id = Column(Integer, nullable=True)
    pipe_catalog = Column(Text, nullable=True)
    is_autoingest_enabled = Column(String(3), nullable=True)
    notification_channel_name = Column(Text, nullable=True)
    pipe_owner = Column(Text, nullable=True)
    definition = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    comment = Column(Text, nullable=True)
    pattern = Column(Text, nullable=True)
    deleted = Column(TIMESTAMP, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEPIPES({})>".format(self.id)


class AccountUsagePipeUsageHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_PIPE_USAGE_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_account_usage_pipe_usage_history'), primary_key=True, autoincrement=True)
    pipe_id = Column(Integer, nullable=True)
    pipe_name = Column(Text, nullable=True)
    pipe_schema_id = Column(Integer, nullable=True)
    pipe_schema = Column(Text, nullable=True)
    pipe_catalog_id = Column(Integer, nullable=True)
    pipe_catalog = Column(Text, nullable=True)
    is_autoingest_enabled = Column(String(3), nullable=True)
    notification_channel_name = Column(Text, nullable=True)
    pipe_owner = Column(Text, nullable=True)
    definition = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    comment = Column(Text, nullable=True)
    pattern = Column(Text, nullable=True)
    deleted = Column(TIMESTAMP, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEPIPEUSAGEHISTORY({})>".format(self.id)


class AccountUsageQueryHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_QUERY_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_account_usage_query_history'), primary_key=True, autoincrement=True)
    query_id = Column(Text, nullable=True)
    query_text = Column(Text, nullable=True)
    database_id = Column(Integer, nullable=True)
    database_name = Column(Text, nullable=True)
    schema_id = Column(Integer, nullable=True)
    schema_name = Column(Text, nullable=True)
    query_type = Column(Text, nullable=True)
    session_id = Column(Integer, nullable=True)
    user_name = Column(Text, nullable=True)
    role_name = Column(Text, nullable=True)
    warehouse_id = Column(Integer, nullable=True)
    warehouse_name = Column(Text, nullable=True)
    warehouse_size = Column(Text, nullable=True)
    warehouse_type = Column(Text, nullable=True)
    cluster_number = Column(Integer, nullable=True)
    query_tag = Column(Text, nullable=True)
    execution_status = Column(Text, nullable=True)
    error_code = Column(Text, nullable=True)
    error_message = Column(Text, nullable=True)
    start_time = Column(TIMESTAMP, nullable=True)
    end_time = Column(TIMESTAMP, nullable=True)
    total_elapsed_time = Column(Integer, nullable=True)
    bytes_scanned = Column(Integer, nullable=True)
    percentage_scanned_from_cache = Column(Float, nullable=True)
    bytes_written = Column(Integer, nullable=True)
    bytes_written_to_result = Column(Integer, nullable=True)
    bytes_read_from_result = Column(Integer, nullable=True)
    rows_produced = Column(Integer, nullable=True)
    rows_inserted = Column(Integer, nullable=True)
    rows_updated = Column(Integer, nullable=True)
    rows_deleted = Column(Integer, nullable=True)
    rows_unloaded = Column(Integer, nullable=True)
    bytes_deleted = Column(Integer, nullable=True)
    partitions_scanned = Column(Integer, nullable=True)
    partitions_total = Column(Integer, nullable=True)
    bytes_spilled_to_local_storage = Column(Integer, nullable=True)
    bytes_spilled_to_remote_storage = Column(Integer, nullable=True)
    bytes_sent_over_the_network = Column(Integer, nullable=True)
    compilation_time = Column(Integer, nullable=True)
    execution_time = Column(Integer, nullable=True)
    queued_provisioning_time = Column(Integer, nullable=True)
    queued_repair_time = Column(Integer, nullable=True)
    queued_overload_time = Column(Integer, nullable=True)
    transaction_blocked_time = Column(Integer, nullable=True)
    outbound_data_transfer_cloud = Column(Text, nullable=True)
    outbound_data_transfer_region = Column(Text, nullable=True)
    outbound_data_transfer_bytes = Column(Integer, nullable=True)
    inbound_data_transfer_cloud = Column(Text, nullable=True)
    inbound_data_transfer_region = Column(Text, nullable=True)
    inbound_data_transfer_bytes = Column(Integer, nullable=True)
    list_external_files_time = Column(Integer, nullable=True)
    credits_used_cloud_services  = Column(Float, nullable=True)
    release_version = Column(Text, nullable=True)
    external_function_total_invocations = Column(Integer, nullable=True)
    external_function_total_sent_rows = Column(Integer, nullable=True)
    external_function_total_received_rows = Column(Integer, nullable=True)
    external_function_total_sent_bytes = Column(Integer, nullable=True)
    external_function_total_received_bytes = Column(Integer, nullable=True)
    query_load_percent = Column(Integer, nullable=True)
    is_client_generated_statement = Column(Boolean, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEQUERYHISTORY({})>".format(self.id)


class AccountUsageReferentialConstraints(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_REFERENTIAL_CONSTRAINTS
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_referential_constraints'), primary_key=True, autoincrement=True)
    constraint_catalog_id = Column(Integer, nullable=True)
    constraint_catalog = Column(Text, nullable=True)
    constraint_schema_id = Column(Integer, nullable=True)
    constraint_schema = Column(Text, nullable=True)
    constraint_name = Column(Text, nullable=True)
    unique_constraint_catalog_id = Column(Integer, nullable=True)
    unique_constraint_catalog = Column(Text, nullable=True)
    unique_constraint_schema_id = Column(Integer, nullable=True)
    unique_constraint_schema = Column(Text, nullable=True)
    unique_constraint_name = Column(Text, nullable=True)
    match_option = Column(Text, nullable=True)
    update_rule = Column(Text, nullable=True)
    delete_rule = Column(Text, nullable=True)
    comment = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    deleted = Column(TIMESTAMP, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEREFERENTIALCONSTRAINTS({})>".format(self.id)


class AccountUsageReplicationUsageHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_REPLICATION_USAGE_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_replication_usage_history'), primary_key=True, autoincrement=True)
    start_time = Column(TIMESTAMP, nullable=True)
    end_time = Column(TIMESTAMP, nullable=True)
    database_name = Column(Text, nullable=True)
    database_id = Column(Integer, nullable=True)
    credits_used = Column(Integer, nullable=True)
    bytes_transferred = Column(Integer, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEREPLICATIONUSAGEHISTORY({})>".format(self.id)


class AccountUsageRoles(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_ROLES
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_role'), primary_key=True, autoincrement=True)
    created_on = Column(TIMESTAMP, nullable=True)
    deleted_on = Column(TIMESTAMP, nullable=True)
    name = Column(Text, nullable=True)
    comment = Column(Text, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEROLES({})>".format(self.id)


class AccountUsageSchemata(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_SCHEMATA
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_schemata'), primary_key=True, autoincrement=True)
    schema_id = Column(Integer, nullable=True)
    schema_name = Column(Text, nullable=True)
    catalog_id = Column(Integer, nullable=True)
    catalog_name = Column(Text, nullable=True)
    schema_owner = Column(Text, nullable=True)
    retention_time = Column(Integer, nullable=True)
    is_transient = Column(String(3), nullable=True)
    is_managed_access = Column(String(3), nullable=True)
    default_character_set_catalog = Column(Text, nullable=True)
    default_character_set_schema = Column(Text, nullable=True)
    default_character_set_name = Column(Text, nullable=True)
    sql_path = Column(Text, nullable=True)
    comment = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    deleted = Column(TIMESTAMP, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGESCHEMATA({})>".format(self.id)


class AccountUsageSearchOptimizationHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_SEARCH_OPTIMIZATION_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_search_optimization_history'), primary_key=True, autoincrement=True)
    start_time = Column(TIMESTAMP, nullable=True)
    end_time = Column(TIMESTAMP, nullable=True)
    credits_used = Column(Integer, nullable=True)
    table_id = Column(Integer, nullable=True)
    table_name = Column(Text, nullable=True)
    schema_id = Column(Integer, nullable=True)
    schema_name = Column(Text, nullable=True)
    database_id = Column(Integer, nullable=True)
    database_name = Column(Text, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<AccountUsageSearchOptimizationHistory({})>".format(self.id)


class AccountUsageSequences(Base):
    
    __tablename__ =  constants.TABLE_ACCOUNT_USAGE_SEQUENCES
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_sequences'), primary_key=True, autoincrement=True)
    sequence_id = Column(Integer, nullable=True)
    sequence_name = Column(Text, nullable=True)
    sequence_schema_id = Column(Integer, nullable=True)
    sequence_schema = Column(Text, nullable=True)
    sequence_catalog_id = Column(Integer, nullable=True)
    sequence_catalog = Column(Text, nullable=True)
    sequence_owner = Column(Text, nullable=True)
    data_type = Column(String(6), nullable=True)
    numeric_precision = Column(Integer, nullable=True)
    numeric_precision_radix = Column(Integer, nullable=True)
    numeric_scale = Column(Integer, nullable=True)
    start_value = Column(Text, nullable=True)
    minimum_value = Column(String(19), nullable=True)
    maximum_value = Column(String(19), nullable=True)
    next_value = Column(Text, nullable=True)
    increment = Column(Text, nullable=True)
    cycle_option = Column(String(2), nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    deleted = Column(TIMESTAMP, nullable=True)
    comment = Column(Text, nullable=True)             
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGESEQUENCES({})>".format(self.id)


class AccountUsageStages(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_STAGES
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_stages'), primary_key=True, autoincrement=True)
    stage_id = Column(Integer, nullable=True)
    stage_name = Column(Text, nullable=True)
    stage_schema_id = Column(Integer, nullable=True)
    stage_schema = Column(Text, nullable=True)
    stage_catalog_id = Column(Integer, nullable=True)
    stage_catalog = Column(Text, nullable=True)
    stage_url = Column(Text, nullable=True)
    stage_region = Column(Text, nullable=True)
    stage_type = Column(Text, nullable=True)
    stage_owner = Column(Text, nullable=True)
    comment = Column(Text, nullable=True)
    created = Column(Text, nullable=True) 
    last_altered = Column(Text, nullable=True) 
    deleted = Column(Text, nullable=True) 
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGESTAGES({})>".format(self.id)


class AccountUsageStageStorageUsageHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_STAGE_STORAGE_USAGE_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_stage_storage_usage_history'), primary_key=True, autoincrement=True)
    usage_date = Column(Date, nullable=True)
    average_stage_bytes = Column(Integer, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGESTAGESTORAGEUSAGEHISTORY({})>".format(self.id)


class AccountUsageStorageUsage(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_STORAGE_USAGE
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_storage_usage'), primary_key=True, autoincrement=True)
    usage_date = Column(Date)
    storage_bytes = Column(Integer, nullable=True)
    stage_bytes = Column(Integer, nullable=True)
    failsafe_bytes = Column(Integer, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGESTORAGEUSAGE({})>".format(self.id)


class AccountUsageTables(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_TABLES
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_tables'), primary_key=True, autoincrement=True)
    table_id = Column(Integer, nullable=True)
    table_name = Column(Text, nullable=True)
    table_schema_id = Column(Integer, nullable=True)
    table_schema = Column(Text, nullable=True)
    table_catalog_id = Column(Integer, nullable=True)
    table_catalog = Column(Text, nullable=True)
    table_owner = Column(Text, nullable=True)
    table_type = Column(Text, nullable=True)
    is_transient = Column(String(3), nullable=True)
    clustering_key = Column(Text, nullable=True)
    row_count = Column(Integer, nullable=True)
    bytes = Column(Integer, nullable=True)
    retention_time = Column(Integer, nullable=True)
    self_referencing_column_name = Column(Text, nullable=True)
    reference_generation = Column(Text, nullable=True)
    user_defined_type_catalog = Column(Text, nullable=True)
    user_defined_type_schema = Column(Text, nullable=True)
    user_defined_type_name = Column(Text, nullable=True)
    is_insertable_into = Column(String(3), nullable=True)
    is_typed = Column(String(3), nullable=True)
    commit_action = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    deleted = Column(TIMESTAMP, nullable=True)
    auto_clustering_on = Column(String(3), nullable=True)
    comment = Column(Text, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGETABLES({})>".format(self.id)



class AccountUsageTableConstraints(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_TABLE_CONSTRAINTS
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_table_constraints'), primary_key=True, autoincrement=True)
    constraint_id = Column(Integer, nullable=True)
    constraint_name = Column(Text, nullable=True)
    constraint_schema_id = Column(Integer, nullable=True)
    constraint_schema = Column(Text, nullable=True)
    constraint_catalog_id = Column(Integer, nullable=True)
    constraint_catalog = Column(Text, nullable=True)
    table_id = Column(Integer, nullable=True)
    table_name = Column(Text, nullable=True)
    table_schema_id = Column(Integer, nullable=True)
    table_schema = Column(Text, nullable=True)
    table_catalog_id = Column(Integer, nullable=True)
    table_catalog = Column(Text, nullable=True)
    constraint_type = Column(Text, nullable=True)
    is_deferrable = Column(String(3), nullable=True)
    initially_deferred = Column(String(3), nullable=True)
    enforced = Column(String(3), nullable=True)
    comment = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    deleted = Column(TIMESTAMP, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<AccountUsageTableConstraints({})>".format(self.id)


class AccountUsageStorageMetrics(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_TABLE_STORAGE_METRICS
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    storage_metric_id = Column(Integer, Sequence('id_acccount_usage_storage_metric'), primary_key=True, autoincrement=True)
    id = Column(Integer, nullable=True)
    table_name = Column(Text, nullable=True)
    table_schema_id = Column(Integer, nullable=True)
    table_schema = Column(Text, nullable=True)
    table_catalog_id = Column(Integer, nullable=True)
    table_catalog = Column(Text, nullable=True)
    clone_group_id = Column(Integer, nullable=True)
    is_transient = Column(String(3), nullable=True)
    active_bytes = Column(Integer, nullable=True)
    time_travel_bytes = Column(Integer, nullable=True)
    failsafe_bytes = Column(Integer, nullable=True)
    retained_for_clone_bytes = Column(Integer, nullable=True)
    deleted = Column(Boolean, nullable=True)
    table_created = Column(TIMESTAMP, nullable=True)
    table_dropped = Column(TIMESTAMP, nullable=True)
    table_entered_failsafe = Column(TIMESTAMP, nullable=True)
    schema_created = Column(TIMESTAMP, nullable=True)
    schema_dropped = Column(TIMESTAMP, nullable=True)
    catalog_created = Column(TIMESTAMP, nullable=True)
    catalog_dropped = Column(TIMESTAMP, nullable=True)
    comment = Column(Text, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGESTORAGEMETRICS({})>".format(self.id)


class AccountUsageUsers(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_USERS
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_users'), primary_key=True, autoincrement=True)
    name = Column(Text, nullable=True)
    created_on = Column(TIMESTAMP, nullable=True)
    deleted_on = Column(TIMESTAMP, nullable=True)
    login_name = Column(Text, nullable=True)
    display_name = Column(Text, nullable=True)
    first_name = Column(Text, nullable=True)
    last_name = Column(Text, nullable=True)
    email = Column(Text, nullable=True)
    must_change_password = Column(Boolean, nullable=True)
    has_password = Column(Boolean, nullable=True)
    comment = Column(Text, nullable=True)
    disabled = Column(VARIANT, nullable=True)
    snowflake_lock = Column(VARIANT, nullable=True)
    default_warehouse = Column(Text, nullable=True)
    default_namespace = Column(Text, nullable=True)
    default_role = Column(Text, nullable=True)
    ext_authn_duo = Column(VARIANT, nullable=True)
    ext_authn_uid = Column(Text, nullable=True)
    bypass_mfa_until = Column(TIMESTAMP, nullable=True)
    last_success_login = Column(TIMESTAMP, nullable=True)
    expires_at = Column(TIMESTAMP, nullable=True)
    locked_until_time = Column(TIMESTAMP, nullable=True)
    has_rsa_public_key = Column(Boolean, nullable=True)
    password_last_set_time = Column(TIMESTAMP, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEUSERS({})>".format(self.id)


class AccountUsageViews(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_VIEWS
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_views'), primary_key=True, autoincrement=True)
    table_id = Column(Integer, nullable=True)
    table_name = Column(Text, nullable=True)
    table_schema_id = Column(Integer, nullable=True)
    table_schema = Column(Text, nullable=True)
    table_catalog_id = Column(Integer, nullable=True)
    table_catalog = Column(Text, nullable=True)
    table_owner = Column(Text, nullable=True)
    view_definition = Column(Text, nullable=True)
    check_option = Column(String(4), nullable=True)
    is_updatable = Column(String(2), nullable=True)
    insertable_into = Column(String(2), nullable=True)
    is_secure = Column(String(3), nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    deleted = Column(TIMESTAMP, nullable=True)
    comment = Column(Text, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEVIEWS({})>".format(self.id)


class AccountUsageWarehouseLoadHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_WAREHOUSE_LOAD_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_warehouse_load_history'), primary_key=True, autoincrement=True)
    start_time = Column(TIMESTAMP, nullable=True)
    end_time = Column(TIMESTAMP, nullable=True)
    warehouse_id = Column(Integer, nullable=True)
    warehouse_name = Column(Text, nullable=True)
    avg_running = Column(Integer, nullable=True)
    avg_queued_load = Column(Integer, nullable=True)
    avg_queued_provisioning = Column(Integer, nullable=True)
    avg_blocked = Column(Integer, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ACCOUNTUSAGEWAREHOUSELOADHISTORY({})>".format(self.id)


class AccountUsageWarehouseMeteringHistory(Base):
    
    __tablename__ = constants.TABLE_ACCOUNT_USAGE_WAREHOUSE_METERING_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_acccount_usage_warehouse_metering_history'), primary_key=True, autoincrement=True)
    start_time = Column(TIMESTAMP, nullable=True)
    end_time = Column(TIMESTAMP, nullable=True)
    warehouse_id = Column(Integer, nullable=True)
    warehouse_name = Column(Text, nullable=True)
    credits_used = Column(Integer, nullable=True)
    credits_used_compute = Column(Integer, nullable=True)
    credits_used_cloud_services = Column(Integer, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<AccountUsageWarehouseMeteringHistory({})>".format(self.id)


class OrganizationUsagePreviewDataTransferDailyHistory(Base):
    
    __tablename__ = constants.TABLE_ORGANIZATION_USAGE_PREVIEW_DATA_TRANSFER_DAILY_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_organization_usage_preview_data_transfer_daily_history'), primary_key=True, autoincrement=True)
    service_type = Column(String(13), nullable=True)
    organization_name = Column(Text, nullable=True)
    account_name = Column(Text, nullable=True)
    usage_date = Column(Date, nullable=True)
    tb_transfered = Column(Float, nullable=True)
    region = Column(Text, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ORGANIZATIONUSAGEPREVIEWDATATRANSFERDAILYHISTORY({})>".format(self.id)


class OrganizationUsagePreviewMeteringDailyHistory(Base):
    
    __tablename__ = constants.TABLE_ORGANIZATION_USAGE_PREVIEW_METERING_DAILY_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_organization_usage_preview_metering_daily_history'), primary_key=True, autoincrement=True)
    service_type = Column(String(25), nullable=True)
    organization_name = Column(Text, nullable=True)
    account_name = Column(Text, nullable=True)
    usage_date = Column(Date, nullable=True)
    credits_used_compute = Column(Integer, nullable=True)
    credits_used_cloud_services = Column(Integer, nullable=True)
    credits_used = Column(Integer, nullable=True)
    credits_adjustment_cloud_services = Column(Integer, nullable=True)
    credits_billed = Column(Integer, nullable=True)
    region = Column(Text, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ORGANIZATIONUSAGEPREVIEWMETERINGDAILYHISTORY({})>".format(self.id)


class OrganizationUsagePreviewStorageDailyHistory(Base):
    
    __tablename__ = constants.TABLE_ORGANIZATION_USAGE_PREVIEW_STORAGE_DAILY_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_organization_usage_preview_storage_daily_history'), primary_key=True, autoincrement=True)
    service_type = Column(String(25), nullable=True)
    organization_name = Column(Text, nullable=True)
    account_name = Column(Text, nullable=True)
    usage_date = Column(Date, nullable=True)
    average_bytes = Column(Integer, nullable=True)
    region = Column(Text, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ORGANIZATIONUSAGEPREVIEWSTORAGEDAILYHISTORY({})>".format(self.id)


class ReaderAccountUsageLoginHistory(Base):
    
    __tablename__ = constants.TABLE_READER_ACCOUNT_USAGE_LOGIN_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_reader_account_usage_login_history'), primary_key=True, autoincrement=True)
    reader_account_name = Column(Text, nullable=True)
    event_id = Column(Integer, nullable=True)
    event_timestamp = Column(TIMESTAMP, nullable=True)
    event_type = Column(Text, nullable=True)
    user_name = Column(Text, nullable=True)
    client_ip = Column(Text, nullable=True)
    reported_client_type = Column(Text, nullable=True)
    reported_client_version = Column(Text, nullable=True)
    first_authentication_factor = Column(Text, nullable=True)
    second_authentication_factor = Column(Text, nullable=True)
    is_success = Column(String(3), nullable=True)
    error_code = Column(Integer, nullable=True)
    error_message = Column(Text, nullable=True)
    related_event_id = Column(Integer, nullable=True)
    reader_account_deleted_on = Column(TIMESTAMP, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<ReaderAccountUsageLoginHistory({})>".format(self.id)


class ReaderAccountUsageQueryHistory(Base):
    
    __tablename__ = constants.TABLE_READER_ACCOUNT_USAGE_QUERY_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_reader_account_usage_query_history'), primary_key=True, autoincrement=True)
    reader_account_name = Column(Text, nullable=True)
    query_id = Column(Text, nullable=True)
    query_text = Column(Text, nullable=True)
    query_type = Column(Text, nullable=True)
    session_id = Column(Integer, nullable=True)
    user_name = Column(Text, nullable=True)
    role_name = Column(Text, nullable=True)
    schema_id = Column(Integer, nullable=True)
    schema_name = Column(Text, nullable=True)
    database_id = Column(Integer, nullable=True)
    database_name = Column(Text, nullable=True)
    warehouse_id = Column(Integer, nullable=True)
    warehouse_name = Column(Text, nullable=True)
    warehouse_size = Column(Text, nullable=True)
    warehouse_type = Column(Text, nullable=True)
    cluster_number = Column(Integer, nullable=True)
    query_tag = Column(Text, nullable=True)
    execution_status = Column(Text, nullable=True)
    error_code = Column(Text, nullable=True)
    error_message = Column(Text, nullable=True)
    start_time= Column(TIMESTAMP, nullable=True)
    end_time= Column(TIMESTAMP, nullable=True)
    total_elapsed_time = Column(Integer, nullable=True)
    bytes_scanned = Column(Integer, nullable=True)
    rows_produced = Column(Integer, nullable=True)
    compilation_time = Column(Integer, nullable=True)
    execution_time = Column(Integer, nullable=True)
    queued_provisioning_time = Column(VARIANT, nullable=True)
    queued_repair_time = Column(VARIANT, nullable=True)
    queued_overload_time = Column(VARIANT, nullable=True)
    transaction_blocked_time = Column(VARIANT, nullable=True)
    outbound_data_transfer_cloud = Column(Text, nullable=True)
    outbound_data_transfer_region = Column(Text, nullable=True)
    outbound_data_transfer_bytes = Column(Integer, nullable=True)
    inbound_data_transfer_cloud = Column(Text, nullable=True)
    inbound_data_transfer_region = Column(Text, nullable=True)
    inbound_data_transfer_bytes = Column(Integer, nullable=True)
    list_external_files_time = Column(Integer, nullable=True)
    credits_used_cloud_services = Column(Float, nullable=True)
    reader_account_deleted_on= Column(TIMESTAMP, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<READERACCOUNTQUERYHISTORY({})>".format(self.id)


class ReaderAccountUsageResourceMonitor(Base):
    
    __tablename__ = constants.TABLE_READER_ACCOUNT_USAGE_RESOURCE_MONITORS
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_reader_account_usage_resource_monitor'), primary_key=True, autoincrement=True)
    reader_account_name  = Column(Text, nullable=True)
    name = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    credit_quota = Column(VARIANT, nullable=True)
    used_credits = Column(VARIANT, nullable=True)
    remaining_credits = Column(Float, nullable=True)
    owner = Column(Text, nullable=True)
    warehouses = Column(Text, nullable=True)
    notify = Column(Integer, nullable=True)
    suspend = Column(Integer, nullable=True)
    suspend_immediate = Column(Integer, nullable=True)
    level = Column(String(9), nullable=True)
    reader_account_deleted_on = Column(TIMESTAMP, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<READERACCOUNTUSAGERESOURCEMONITOR({})>".format(self.id)


class ReaderAccountUsageStorageUsage(Base):
    
    __tablename__ = constants.TABLE_READER_ACCOUNT_USAGE_STORAGE_USAGE
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_reader_account_usage_storage_usage'), primary_key=True, autoincrement=True)
    reader_account_name = Column(Text, nullable=True)
    usage_date = Column(Date, nullable=True)
    storage_bytes = Column(Integer, nullable=True)
    stage_bytes = Column(Integer, nullable=True)
    failsafe_bytes = Column(Integer, nullable=True)
    reader_account_deleted_on = Column(TIMESTAMP, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<READERACCOUNTUSAGESTORAGEUSAGE({})>".format(self.id)


class ReaderAccountUsageWarehouseMeteringHistory(Base):
    
    __tablename__ = constants.TABLE_READER_ACCOUNT_USAGE_WAREHOUSE_METERING_HISTORY
    __table_args__ = {
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_reader_account_usage_warehouse_metering_history'), primary_key=True, autoincrement=True)
    reader_account_name = Column(Text, nullable=True)
    start_time = Column(TIMESTAMP, nullable=True)
    end_time = Column(TIMESTAMP, nullable=True)
    warehouse_id = Column(Integer, nullable=True)
    warehouse_name = Column(Text, nullable=True)
    credits_used = Column(Integer, nullable=True)
    credits_used_compute = Column(Integer, nullable=True)
    credits_used_cloud_services = Column(Integer, nullable=True)
    reader_account_deleted_on = Column(TIMESTAMP, nullable=True)
    event = Column(Text, nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    date_run = Column(Date)

    def __repr__(self):
        #return the class object.
        return "<READERACCOUNTUSAGEWAREHOUSEMETERINGHISTORY({})>".format(self.id)


#create tables.
# Base.metadata.create_all(engine)

#dispose engine
# dispose_engine = DisposeEngine(engine= engine)