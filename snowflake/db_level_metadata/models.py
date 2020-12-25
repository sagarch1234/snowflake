import os
import sys
import datetime

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
# connector = SnowflakeConnector(user=os.environ.get('SNOWFLAKE_ACCOUNT_USER'), password=os.environ.get('SNOWFLAKE_ACCOUNT_PASSWORD'), account=os.environ.get('SNOWFLAKE_ACCOUNT'), database_name=os.environ.get('SNOWFLAKE_DATABASE_NAME'), schema_name=os.environ.get('SCHEMA_NAME_AUDITS'), role=os.environ.get('ACCOUNT_ROLE'), warehouse=os.environ.get('ACCOUNT_WAREHOUSE'))

#get engine
# engine = connector.get_engine()

class InfoSchemaApplicableRoles(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_APPLICABLE_ROLES
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_parameters_in_database'), autoincrement=True)
    grantee = Column(Text, nullable=True)
    role_name = Column(Text, nullable=True)
    role_owner = Column(Text, nullable=True)
    is_grantable = Column(String(3), nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Applicable Roles({})>".format(self.id)



class InfoSchemaColumns(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_COLUMNS
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_columns'), autoincrement=True)
    table_catalog = Column(Text, nullable=True)
    table_schema = Column(Text, nullable=True)
    table_name = Column(Text, nullable=True)
    column_name = Column(Text, nullable=True)
    ordinal_position = Column(Integer, nullable=True)
    column_default = Column(Text, nullable=True)
    is_nullable = Column(String(3), nullable=True)
    data_type = Column(Text, nullable=True)
    character_maximum_length = Column(Integer, nullable=True)
    character_octet_length = Column(Integer, nullable=True)
    numeric_precision = Column(Integer, nullable=True)
    numeric_precision_radix = Column(Integer, nullable=True)
    numeric_scale = Column(Integer, nullable=True)
    datetime_precision = Column(Integer, nullable=True)
    interval_type = Column(Text, nullable=True)
    interval_precision = Column(Integer, nullable=True)
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
    maximum_cardinality = Column(Integer, nullable=True)
    dtd_identifier = Column(Text, nullable=True)
    is_self_referencing = Column(String(3), nullable=True)
    is_identity = Column(String(3), nullable=True)
    identity_generation = Column(Text, nullable=True)
    identity_start = Column(Text, nullable=True)
    identity_increment = Column(Text, nullable=True)
    identity_maximum = Column(Text, nullable=True)
    identity_minimum = Column(Text, nullable=True)
    identity_cycle = Column(Text, nullable=True)
    comment = Column(Text, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Applicable Columns({})>".format(self.id)


class InfoSchemaDatabases(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_DATABASES
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_databases'), autoincrement=True)
    database_name = Column(Text, nullable=True)
    database_owner = Column(Text, nullable=True)
    is_transient = Column(String(3), nullable=True)
    comment = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    retention_time = Column(Integer, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Databases({})>".format(self.id)


class InfoSchemaEnabledRoles(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_ENABLED_ROLES
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_enabled_roles'), autoincrement=True)
    role_name = Column(Text, nullable=True)
    role_owner = Column(Text, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Enabled Roles({})>".format(self.id)


class InfoSchemaExternalTables(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_EXTERNAL_TABLES
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_external_tables'), autoincrement=True)
    table_catalog = Column(Text, nullable=True)
    table_schema = Column(Text, nullable=True)
    table_name = Column(Text, nullable=True)
    table_owner = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    comment = Column(Text, nullable=True)
    location = Column(Text, nullable=True)
    file_format_name = Column(Text, nullable=True)
    file_format_type = Column(Text, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema External Tables({})>".format(self.id)


class InfoSchemaFileFormats(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_FILE_FORMATS
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_file_formats'), autoincrement=True)
    file_format_catalog = Column(Text, nullable=True)
    file_format_schema = Column(Text, nullable=True)
    file_format_name = Column(Text, nullable=True)
    file_format_owner = Column(Text, nullable=True)
    file_format_type = Column(Text, nullable=True)
    record_delimiter = Column(String(1), nullable=True)
    field_delimiter = Column(String(1), nullable=True)
    skip_header = Column(Integer, nullable=True)
    date_format = Column(Text, nullable=True)
    time_format = Column(Text, nullable=True)
    timestamp_format = Column(Text, nullable=True)
    binary_format = Column(Text, nullable=True)
    escape = Column(String(1), nullable=True)
    escape_unenclosed_field = Column(String(1), nullable=True)
    trim_space = Column(Text, nullable=True)
    field_optionally_enclosed_by = Column(Text, nullable=True)
    null_if = Column(Text, nullable=True)
    compression = Column(Text, nullable=True)
    error_on_column_count_mismatch = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    comment = Column(Text, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema File Formats({})>".format(self.id)


class InfoSchemaFunctions(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_FUNCTIONS
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_functions'), autoincrement=True)
    function_catalog = Column(Text, nullable=True)
    function_schema = Column(Text, nullable=True)
    function_name = Column(Text, nullable=True)
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
    is_null_call = Column(String(3), nullable=True)
    is_secure = Column(String(3), nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    comment = Column(Text, nullable=True)
    is_external = Column(String(3), nullable=True)
    api_integration = Column(Text, nullable=True)
    context_headers = Column(Text, nullable=True)
    max_batch_rows = Column(Integer, nullable=True)
    compression = Column(Text, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Functions({})>".format(self.id)
    

class InfoSchemaCatlogName(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_CATALOG_NAME
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_catlog_name'), autoincrement=True)
    catalog_name = Column(Text, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Catlog Name({})>".format(self.id)


class InfoSchemaLoadHistory(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_LOAD_HISTORY
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_load_history'), autoincrement=True)
    schema_name = Column(Text, nullable=True)
    file_name = Column(Text, nullable=True)
    table_name = Column(Text, nullable=True)
    last_load_time = Column(TIMESTAMP, nullable=True)
    status = Column(Text, nullable=True)
    row_count = Column(Integer, nullable=True)
    row_parsed = Column(Integer, nullable=True)
    first_error_message = Column(Text, nullable=True)
    first_error_line_number= Column(Integer, nullable=True)
    first_error_character_position= Column(Integer, nullable=True)
    first_error_col_name = Column(Text, nullable=True)
    error_count= Column(Integer, nullable=True)
    error_limit= Column(Integer, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Load History({})>".format(self.id)


class InfoSchemaObjectPrivileges(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_OBJECT_PRIVILEGES
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_object_privileges'), autoincrement=True)
    grantor = Column(Text, nullable=True)
    grantee = Column(Text, nullable=True)
    object_catalog = Column(Text, nullable=True)
    object_schema = Column(Text, nullable=True)
    object_name = Column(Text, nullable=True)
    object_type = Column(Text, nullable=True)
    privilege_type = Column(Text, nullable=True)
    is_grantable = Column(String(3), nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Object Privileges({})>".format(self.id)



class InfoSchemaPipes(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_PIPES
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_pipes'), autoincrement=True)
    pipe_catalog = Column(Text, nullable=True)
    pipe_schema = Column(Text, nullable=True)
    pipe_name = Column(Text, nullable=True)
    pipe_owner = Column(Text, nullable=True)
    definition = Column(Text, nullable=True)
    is_autoingest_enabled = Column(String(3), nullable=True)
    notification_channel_name = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    comment = Column(Text, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema  Pipes({})>".format(self.id)


class InfoSchemaProcedures(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_PROCEDURES
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_procedures'), autoincrement=True)
    procedure_catalog = Column(Text, nullable=True)
    procedure_schema = Column(Text, nullable=True)
    procedure_name = Column(Text, nullable=True)
    procedure_owner = Column(Text, nullable=True)
    argument_signature = Column(Text, nullable=True)
    data_type = Column(Text, nullable=True)
    character_maximum_length = Column(Integer, nullable=True)
    character_octet_length = Column(Integer, nullable=True)
    numeric_precision = Column(Integer, nullable=True)
    numeric_precision_radix = Column(Integer, nullable=True)
    numeric_scale = Column(Integer, nullable=True)
    procedure_language = Column(Text, nullable=True)
    procedure_definition = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Procedures({})>".format(self.id)


class InfoSchemaReferentialConstraints(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_REFERENTIAL_CONSTRAINTS
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_referential_constraints'), autoincrement=True)
    constraint_catalog = Column(Text, nullable=True)
    constraint_schema = Column(Text, nullable=True)
    constraint_name = Column(Text, nullable=True)
    unique_constraint_catalog = Column(Text, nullable=True)
    unique_constraint_schema = Column(Text, nullable=True)
    unique_constraint_name = Column(Text, nullable=True)
    match_option = Column(Text, nullable=True)
    update_rule = Column(Text, nullable=True)
    delete_rule = Column(Text, nullable=True)
    comment = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Referential Constraints({})>".format(self.id)


class InfoSchemaReplicationDatabases(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_REPLICATION_DATABASES
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_replication_databases'), autoincrement=True)
    region_group = Column(Text, nullable=True)
    snowflake_region = Column(Text, nullable=True)
    account_name = Column(Text, nullable=True)
    database_name = Column(Text, nullable=True)
    comment = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    is_primary = Column(Boolean, nullable=True)
    primary = Column(Text, nullable=True)
    replication_allowed_to_accounts = Column(Text, nullable=True)
    failover_allowed_to_accounts = Column(Text, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Replication Databases({})>".format(self.id)


class InfoSchemaSchemata(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_SCHEMATA
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_schemata'), autoincrement=True)
    catalog_name = Column(Text, nullable=True)
    schema_name = Column(Text, nullable=True)
    schema_owner = Column(Text, nullable=True)
    is_transient = Column(String(3), nullable=True)
    is_managed_access = Column(String(3), nullable=True)
    retention_time = Column(Integer, nullable=True)
    default_character_set_catalog = Column(Text, nullable=True)
    default_character_set_schema = Column(Text, nullable=True)
    default_character_set_name = Column(Text, nullable=True)
    sql_path = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Schemata({})>".format(self.id)


class InfoSchemaSequences(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_SEQUENCES
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_sequences'), autoincrement=True)
    sequence_catalog = Column(Text, nullable=True)
    sequence_schema = Column(Text, nullable=True)
    sequence_name = Column(Text, nullable=True)
    sequence_owner = Column(Text, nullable=True)
    data_type = Column(Text, nullable=True)
    numeric_precision = Column(Integer, nullable=True)
    numeric_precision_radix = Column(Integer, nullable=True)
    numeric_scale = Column(Integer, nullable=True)
    start_value = Column(Text, nullable=True)
    minimum_value = Column(Text, nullable=True)
    maximum_value = Column(Text, nullable=True)
    next_value = Column(Text, nullable=True)
    increment = Column(Text, nullable=True)
    cycle_option = Column(String(3), nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    comment = Column(Text, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Sequences({})>".format(self.id)


class InfoSchemaStages(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_STAGES
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_stages'), autoincrement=True)
    stage_catalog = Column(Text, nullable=True)
    stage_schema = Column(Text, nullable=True)
    stage_name = Column(Text, nullable=True)
    stage_url = Column(Text, nullable=True)
    stage_region = Column(Text, nullable=True)
    stage_type = Column(Text, nullable=True)
    stage_owner = Column(Text, nullable=True)
    comment = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Stages({})>".format(self.id)


class InfoSchemaTables(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_TABLES
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_tables'), autoincrement=True)
    table_catalog = Column(Text, nullable=True)
    table_schema = Column(Text, nullable=True)
    table_name = Column(Text, nullable=True)
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
    auto_clustering_on = Column(String(3), nullable=True)
    comment = Column(Text, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Tables({})>".format(self.id)


class InfoSchemaTablesConstraints(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_TABLE_CONSTRAINTS
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_tables_constraints'), autoincrement=True)
    constraint_catalog = Column(Text, nullable=True)
    constraint_schema = Column(Text, nullable=True)
    constraint_name = Column(Text, nullable=True)
    table_catalog = Column(Text, nullable=True)
    table_schema = Column(Text, nullable=True)
    table_name = Column(Text, nullable=True)
    constraint_type = Column(Text, nullable=True)
    is_deferrable = Column(String(3), nullable=True)
    initially_deferred = Column(String(3), nullable=True)
    enforced = Column(String(3), nullable=True)
    comment = Column(Text, nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Tables Constraints({})>".format(self.id)


class InfoSchemaTablesPrivileges(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_TABLE_PRIVILEGES
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_tables_privileges'), autoincrement=True)
    grantor = Column(Text, nullable=True)
    grantee = Column(Text, nullable=True)
    table_catalog = Column(Text, nullable=True)
    table_schema = Column(Text, nullable=True)
    table_name = Column(Text, nullable=True)
    privilege_type = Column(Text, nullable=True)
    is_grantable = Column(String(3), nullable=True)
    with_hierarchy = Column(String(3), nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Tables Privileges({})>".format(self.id)



class InfoSchemaTablesStorageMetrics(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_TABLE_STORAGE_METRICS
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id_table_metrics = Column(Integer, Sequence('id_info_schema_tables_metrics'), autoincrement=True)
    table_catalog = Column(Text, nullable=True)
    table_schema = Column(Text, nullable=True)
    table_name = Column(Text, nullable=True)
    id = Column(Integer, nullable=True)
    clone_group_id = Column(Integer, nullable=True)
    is_transient = Column(String(3), nullable=True)
    active_bytes = Column(Integer, nullable=True)
    time_travel_bytes = Column(Integer, nullable=True)
    failsafe_bytes = Column(Integer, nullable=True)
    retained_for_clone_bytes = Column(Integer, nullable=True)
    table_created = Column(TIMESTAMP, nullable=True)
    table_dropped = Column(TIMESTAMP, nullable=True)
    table_entered_failsafe = Column(TIMESTAMP, nullable=True)
    catalog_created = Column(TIMESTAMP, nullable=True)
    catalog_dropped = Column(TIMESTAMP, nullable=True)
    schema_created = Column(TIMESTAMP, nullable=True)
    schema_dropped = Column(TIMESTAMP, nullable=True)
    comment = Column(Text, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Tables Storage Metrics({})>".format(self.id)


class InfoSchemaUsagePrivileges(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_USAGE_PRIVILEGES
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_usage_privileges'), autoincrement=True)
    grantor = Column(Text, nullable=True)
    grantee = Column(Text, nullable=True)
    object_catalog = Column(Text, nullable=True)
    object_schema = Column(Text, nullable=True)
    object_name = Column(Text, nullable=True)
    object_type = Column(Text, nullable=True)
    privilege_type = Column(Text, nullable=True)
    is_grantable = Column(String(3), nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Usage Privileges({})>".format(self.id)


class InfoSchemaViews(Base):

    __tablename__ = constants.TABLE_INFORMATION_SCHEMA_VIEWS
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_AUDITS')
    }

    id = Column(Integer, Sequence('id_info_schema_views'), autoincrement=True)
    table_catalog = Column(Text, nullable=True)
    table_schema = Column(Text, nullable=True)
    table_name = Column(Text, nullable=True)
    table_owner = Column(Text, nullable=True)
    view_definition = Column(Text, nullable=True)
    check_option = Column(Text, nullable=True)
    is_updatable = Column(String(3), nullable=True)
    insertable_into = Column(String(3), nullable=True)
    is_secure = Column(String(3), nullable=True)
    created = Column(TIMESTAMP, nullable=True)
    last_altered = Column(TIMESTAMP, nullable=True)
    comment = Column(Text, nullable=True)
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Views({})>".format(self.id)

#create tables.
# Base.metadata.create_all(engine)

#dispose engine
# dispose_engine = DisposeEngine(engine= engine)