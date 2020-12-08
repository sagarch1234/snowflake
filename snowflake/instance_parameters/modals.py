import sys
import datetime
import os

sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')

from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column, Text, Boolean, create_engine, Time, String, Sequence, DateTime
from snowflake.sqlalchemy import URL

from connection import SnowflakeConnector
from connection import DisposeEngine

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

    __tablename__ = 'account_parameters'
    __table_args__ = {
        'schema' : 'os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_account_parameters'), primary_key=True, autoincrement=True)
    key = Column(String(200), nullable=True)
    value = Column(String(200), nullable=True)
    default = Column(String(200), nullable=True)
    level = Column(String(200), nullable=True)
    description = Column(Text)
    type = Column(String(100), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True) 

    def __repr__(self):
        #return the class object.
        return "<AccountParameters({})>".format(self.id)
    

class DatabasesOnInstance(Base):

    '''
    This model will store the databases of the customers instances.
    '''
    __tablename__ = 'instance_databases'
    __table_args__ = {
        'schema' : 'os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_databases_on_instance'), primary_key=True, autoincrement=True)
    created_on = Column(String(200), nullable=True)
    name = Column(String(100), nullable=True)
    is_default = Column(String(50), nullable=True)
    is_current = Column(String(50), nullable=True)
    origin = Column(String(200), nullable=True)
    owner = Column(String(100), nullable=True)
    comment = Column(Text, nullable=True)
    options = Column(String(100), nullable=True)
    retention_time = Column(String(20), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True) 


    def __repr__(self):
        return "<DatabasesOnInstance({})>".format(self.id)


class SchemaOnInstance(Base):

    '''
    This model will store the schema of the customers instances.
    '''
    
    __tablename__ = 'instance_databases_schema'
    __table_args__ = {
        'schema' : 'os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_schema_on_instance'), primary_key=True, autoincrement=True)
    created_on = Column(String(200), nullable=True)
    name = Column(String(100), nullable=True)
    is_default = Column(String(50), nullable=True)
    is_current = Column(String(50), nullable=True)
    database_name = Column(String(200), nullable=True)
    owner = Column(String(100), nullable=True)
    comment = Column(Text, nullable=True)
    options = Column(String(100), nullable=True)
    retention_time = Column(String(20), nullable=True)
    instance_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)
    

    def __repr__(self):
        return "<SchemaOnInstance({})>".format(self.name)


class ParametersInDatabase(Base):

    '''
    This model will store the parameters of each databases fetched from the customers instances.
    '''
    
    __tablename__ = 'parameters_in_database'
    __table_args__ = {
        'schema' : 'os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_parameters_in_database'), primary_key=True, autoincrement=True)
    key = Column(String(200), nullable=True)
    value = Column(String(200), nullable=True)
    default = Column(String(200), nullable=True)
    level = Column(String(200), nullable=True)
    description = Column(Text, nullable=True)
    type = Column(String(100), nullable=True)
    instance_id = Column(Integer, nullable=True) 
    database_name = Column(String(100), nullable=True)
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    # Relationships
    # databases_on_instance = relationship("DatabasesOnInstance")

    def __repr__(self):
        
        return "<ParametersInDatabase({})>".format(self.id)


class ParametersInSchemas(Base):

    '''
    This model will store the parameters of each schema fetched from the customers instances.
    '''
    __tablename__ = 'parameters_in_schemas'
    __table_args__ = {
        # 'extend_existing' : True,
        'schema' : 'os.environ.get('SCHEMA_NAME_PARAMS')
    }

    id = Column(Integer, Sequence('id_parameters_in_schemas'), primary_key=True, autoincrement=True)
    key = Column(String(200), nullable=True)
    value = Column(String(200), nullable=True)
    default = Column(String(200), nullable=True)
    level = Column(String(200), nullable=True)
    description = Column(Text, nullable=True)
    type = Column(String(100), nullable=True)
    database_name = Column(String(100), nullable=True)
    schema_name = Column(String(100), nullable=True)
    instance_id = Column(Integer, nullable=True) 
    company_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    run_date_time = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String(20), nullable=True)

    # Relationships
    # databases_on_instance = relationship("DatabasesOnInstance")
    # schema_on_instance = relationship("SchemaOnInstance")

    def __repr__(self):
        return "<ParametersInSchemas({})>".format(self.id)


#create tables.
# Base.metadata.create_all(engine)

#dispose engine
# dispose_engine = DisposeEngine(engine= engine)