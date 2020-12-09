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
# connector = SnowflakeConnector(user=os.environ.get('SNOWFLAKE_ACCOUNT_USER'), password=os.environ.get('SNOWFLAKE_ACCOUNT_PASSWORD'), account=os.environ.get('SNOWFLAKE_ACCOUNT'), database_name=os.environ.get('SNOWFLAKE_DATABASE_NAME'), schema_name=os.environ.get('SCHEMA_NAME_AUDITS'), role=os.environ.get('ACCOUNT_ROLE'), warehouse=os.environ.get('ACCOUNT_WAREHOUSE'))

#get engine
# engine = connector.get_engine()

class InfoSchemaApplicableRoles(Base):

    __tablename__ = 'info_schema_applicable_roles'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_parameters_in_database'), primary_key=True, autoincrement=True)
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

    __tablename__ = 'info_schema_columns'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_columns'), primary_key=True, autoincrement=True)
    
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Applicable Columns({})>".format(self.id)


class InfoSchemaDatabases(Base):

    __tablename__ = 'info_schema_databases'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_databases'), primary_key=True, autoincrement=True)
    
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Databases({})>".format(self.id)


class InfoSchemaEnabledRoles(Base):

    __tablename__ = 'info_schema_enabled_roles'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_enabled_roles'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Enabled Roles({})>".format(self.id)


class InfoSchemaExternalTables(Base):

    __tablename__ = 'info_schema_external_tables'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_external_tables'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema External Tables({})>".format(self.id)


class InfoSchemaFileFormats(Base):

    __tablename__ = 'info_schema_file_formats'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_file_formats'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema File Formats({})>".format(self.id)


class InfoSchemaFunstions(Base):

    __tablename__ = 'info_schema_functions'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_functions'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Functions({})>".format(self.id)
    

class InfoSchemaCatlogName(Base):

    __tablename__ = 'info_schema_catlog_name'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_catlog_name'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Catlog Name({})>".format(self.id)


class InfoSchemaLoadHistory(Base):

    __tablename__ = 'info_schema_load_history'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_load_history'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Load History({})>".format(self.id)


class InfoSchemaObjectPrivileges(Base):

    __tablename__ = 'info_schema_object_privileges'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_object_privileges'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Object Privileges({})>".format(self.id)



class InfoSchemaPipes(Base):

    __tablename__ = 'info_schema_pipes'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_pipes'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema  Pipes({})>".format(self.id)


class InfoSchemaProcedures(Base):

    __tablename__ = 'info_schema_procedures'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_procedures'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Procedures({})>".format(self.id)


class InfoSchemaReferentialConstraints(Base):

    __tablename__ = 'info_schema_referential_constraints'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_referential_constraints'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Referential Constraints({})>".format(self.id)


class InfoSchemaReplicationDatabases(Base):

    __tablename__ = 'info_schema_replication_databases'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_replication_databases'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Replication Databases({})>".format(self.id)


class InfoSchemaSchemata(Base):

    __tablename__ = 'info_schema_schemata'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_schemata'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Schemata({})>".format(self.id)


class InfoSchemaSequences(Base):

    __tablename__ = 'info_schema_sequences'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_sequences'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Sequences({})>".format(self.id)


class InfoSchemaStages(Base):

    __tablename__ = 'info_schema_stages'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_stages'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Stages({})>".format(self.id)


class InfoSchemaTables(Base):

    __tablename__ = 'info_schema_tables'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_tables'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Tables({})>".format(self.id)


class InfoSchemaTablesConstraints(Base):

    __tablename__ = 'info_schema_tables_constraints'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_tables_constraints'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Tables Constraints({})>".format(self.id)


class InfoSchemaTablesPrivileges(Base):

    __tablename__ = 'info_schema_tables_privileges'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_tables_privileges'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Tables Privileges({})>".format(self.id)



class InfoSchemaTablesStorageMetrics(Base):

    __tablename__ = 'info_schema_tables_metrics'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_tables_metrics'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Tables Storage Metrics({})>".format(self.id)


class InfoSchemaUsagePrivileges(Base):

    __tablename__ = 'info_schema_usage_privileges'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_usage_privileges'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Usage Privileges({})>".format(self.id)


class InfoSchemaViews(Base):

    __tablename__ = 'info_schema_views'
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_info_schema_views'), primary_key=True, autoincrement=True)

    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    def __repr__(self):
        #return the class object.
        return "<Info Schema Views({})>".format(self.id)