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
# connector = SnowflakeConnector(user=os.environ.get('SNOWFLAKE_ACCOUNT_USER'), password=os.environ.get('SNOWFLAKE_ACCOUNT_PASSWORD'), account=os.environ.get('SNOWFLAKE_ACCOUNT'), database_name=os.environ.get('SNOWFLAKE_DATABASE_NAME'), schema_name=os.environ.get('SCHEMA_NAME_PARAMS'), role=os.environ.get('ACCOUNT_ROLE'), warehouse=os.environ.get('ACCOUNT_WAREHOUSE'))

#get engine
# engine = connector.get_engine()


class AccountParameters(Base):
    
    '''
    This model will store the account parameters of the customers instances.
    '''

    __tablename__ = constants.TABLE_ACCOUNT_PARAMETERS
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS'),
        'extend_existing' : True
    }

    id = Column('id', Integer, Sequence('id_account_parameters'), primary_key=True)
    key = Column('key', String(200), nullable=True)
    value = Column('value', String(200), nullable=True)
    default = Column('default', String(200), nullable=True)
    level = Column('level', String(200), nullable=True)
    description = Column('description', Text)
    type = Column('type', String(100), nullable=True)
    instance_id = Column('instance_id', Integer, nullable=True)
    company_id = Column('company_id', Integer, nullable=True)
    user_id = Column('user_id', Integer, nullable=True)
    run_date_time = Column('run_date_time', DateTime, default=datetime.datetime.utcnow)
    event = Column('event', String(20), nullable=True) 

    def __repr__(self):
        #return the class object.
        return "<AccountParameters({})>".format(self.id)
    

class InstanceDatabases(Base):

    '''
    This model will store the databases of the customers instances.
    '''
    __tablename__ = constants.TABLE_DATABASES
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS'),
        'extend_existing' : True
    }

    id = Column("id", Integer, Sequence('id_databases_on_instance'), primary_key=True)
    created_on = Column("created_on", TIMESTAMP, nullable=True)
    name = Column("name", String(100), nullable=True)
    is_default = Column("is_default", String(50), nullable=True)
    is_current = Column("is_current", String(50), nullable=True)
    origin = Column("origin", String(200), nullable=True)
    owner = Column("owner", String(100), nullable=True)
    comment = Column("comment", Text, nullable=True)
    options = Column("optoins", String(100), nullable=True)
    retention_time = Column("retention_time", String(20), nullable=True)
    instance_id = Column("instance_id", Integer, nullable=True)
    company_id = Column("company_id", Integer, nullable=True)
    user_id = Column("user_id", Integer, nullable=True)
    run_date_time = Column("run_date_time", DateTime, default=datetime.datetime.utcnow)
    event = Column("event", String(20), nullable=True) 


    def __repr__(self):
        return "<DatabasesOnInstance({})>".format(self.id)


class InstanceDatabasesSchemas(Base):

    '''
    This model will store the schema of the customers instances.
    '''
    
    __tablename__ = constants.TABLE_SCHEMAS
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS'),
        'extend_existing' : True
    }

    id = Column("id",Integer, Sequence('id_schema_on_instance'), primary_key=True)
    created_on = Column("created_on",TIMESTAMP, nullable=True)
    name = Column("name",String(100), nullable=True)
    is_default = Column("is_default",String(50), nullable=True)
    is_current = Column("is_current",String(50), nullable=True)
    database_name = Column("database_name",String(200), nullable=True)
    owner = Column("owner",String(100), nullable=True)
    comment = Column("comment",Text, nullable=True)
    options = Column("options",String(100), nullable=True)
    retention_time = Column("retention_time",String(20), nullable=True)
    instance_id = Column("instance_id",Integer, nullable=True)
    company_id = Column("company_id",Integer, nullable=True)
    user_id = Column("user_id",Integer, nullable=True)
    run_date_time = Column("run_date_time",DateTime, default=datetime.datetime.utcnow)
    event = Column("event",String(20), nullable=True)
    

    def __repr__(self):
        return "<SchemaOnInstance({})>".format(self.name)


class ParametersInDatabase(Base):

    '''
    This model will store the parameters of each databases fetched from the customers instances.
    '''
    
    __tablename__ = constants.TABLE_DB_LEVEL_PARAMETERS
    __table_args__ = {
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS'),
        'extend_existing' : True
    }

    id = Column("id", Integer, Sequence('id_parameters_in_database'), primary_key=True)
    key = Column("key", String(200), nullable=True)
    value = Column("value", String(200), nullable=True)
    default = Column("default", String(200), nullable=True)
    level = Column("level", String(200), nullable=True)
    description = Column("description", Text, nullable=True)
    type = Column("type", String(100), nullable=True)
    instance_id = Column("instance_id", Integer, nullable=True) 
    database_name = Column("database_name", String(100), nullable=True)
    company_id = Column("company_id", Integer, nullable=True)
    user_id = Column("user_id", Integer, nullable=True)
    run_date_time = Column("run_date_time",DateTime, default=datetime.datetime.utcnow)
    event = Column("event", String(20), nullable=True)

    # Relationships
    # databases_on_instance = relationship("DatabasesOnInstance")

    def __repr__(self):
        
        return "<ParametersInDatabase({})>".format(self.id)


class ParametersInSchemas(Base):

    '''
    This model will store the parameters of each schema fetched from the customers instances.
    '''
    __tablename__ = constants.TABLE_SCHEMA_PARAMETERS
    __table_args__ = {
        # 'extend_existing' : True,
        'schema' : os.environ.get('SCHEMA_NAME_PARAMS'),
        'extend_existing' : True
    }

    id = Column("id",Integer, Sequence('id_parameters_in_schemas'), primary_key=True)
    key = Column("key",String(200), nullable=True)
    value = Column("value",String(200), nullable=True)
    default = Column("default",String(200), nullable=True)
    level = Column("level",String(200), nullable=True)
    description = Column("description",Text, nullable=True)
    type = Column("type",String(100), nullable=True)
    database_name = Column("database_name",String(100), nullable=True)
    schema_name = Column("schema_name",String(100), nullable=True)
    instance_id = Column("instance_id",Integer, nullable=True) 
    company_id = Column("company_id",Integer, nullable=True)
    user_id = Column("user_id",Integer, nullable=True)
    run_date_time = Column("run_date_time",DateTime, default=datetime.datetime.utcnow)
    event = Column("event",String(20), nullable=True)

    # Relationships
    # databases_on_instance = relationship("DatabasesOnInstance")
    # schema_on_instance = relationship("SchemaOnInstance")

    def __repr__(self):
        return "<ParametersInSchemas({})>".format(self.id)


#create tables.
# Base.metadata.create_all(engine)

#dispose engine
# dispose_engine = DisposeEngine(engine= engine)