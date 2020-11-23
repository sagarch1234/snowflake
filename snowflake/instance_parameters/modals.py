import sys

sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')

from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column, Text, Boolean, ForeignKey, create_engine, Time, String, Sequence
from snowflake.sqlalchemy import URL

from connection import SnowflakeConnector

#using declarative base
Base = declarative_base()

#get SnowflakeConnector class object
connector = SnowflakeConnector(user='SFOPT_TEST_APP', password='(sE&Gv]82qv^3KJU', account='ya78377.east-us-2.azure', database_name='SFOPT_TEST', schema_name='SFOPT_TEST_SCHEMA', role='SFOPT_TEST_APP_ROLE')

#get engine
engine = connector.get_engine()


class AccountParameters(Base):
    '''
    '''
    __tablename__ = 'account_parameters'
    __table_args__ = {
        # 'extend_existing' : True,
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('_idaccount_parameters'), primary_key=True, autoincrement=True)
    key = Column(String(200), nullable=True)
    value = Column(String(200), nullable=True)
    default = Column(String(200), nullable=True)
    level = Column(String(200), nullable=True)
    description = Column(Text)
    type = Column(String(100), nullable=True)
    instance_id = Column(Integer, nullable=True) 

    def __repr__(self):
        return "<AccountParameters({})>".format(self.id)
    

class DatabasesOnInstance(Base):
    '''
    '''
    __tablename__ = 'databases_on_instance'
    __table_args__ = {
        # 'extend_existing' : True,
        'schema' : 'SFOPT_TEST_SCHEMA'
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

    def __repr__(self):
        return "<DatabasesOnInstance({})>".format(self.id)


class SchemaOnInstance(Base):
    '''
    '''
    __tablename__ = 'schema_on_instance'
    __table_args__ = {
        # 'extend_existing' : True,
        'schema' : 'SFOPT_TEST_SCHEMA'
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

    def __repr__(self):
        return "<SchemaOnInstance({})>".format(self.name)


class ParametersInDatabase(Base):
    '''
    '''
    __tablename__ = 'parameters_in_database'
    __table_args__ = {
        # 'extend_existing' : True,
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_parameters_in_database'), primary_key=True, autoincrement=True)
    key = Column(String(200), nullable=True)
    value = Column(String(200), nullable=True)
    default = Column(String(200), nullable=True)
    level = Column(String(200), nullable=True)
    description = Column(Text, nullable=True)
    type = Column(String(100), nullable=True)
    instance_id = Column(Integer, nullable=True) 
    database_id = Column(Integer, ForeignKey(DatabasesOnInstance.id), nullable=True)

    # Relationships
    databases_on_instance = relationship("DatabasesOnInstance")

    def __repr__(self):
        return "<ParametersInDatabase({})>".format(self.id)


class ParametersInSchemas(Base):
    '''
    '''
    __tablename__ = 'parameters_in_schemas'
    __table_args__ = {
        # 'extend_existing' : True,
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, Sequence('id_parameters_in_schemas'), primary_key=True, autoincrement=True)
    key = Column(String(200), nullable=True)
    value = Column(String(200), nullable=True)
    default = Column(String(200), nullable=True)
    level = Column(String(200), nullable=True)
    description = Column(Text, nullable=True)
    type = Column(String(100), nullable=True)
    instance_id = Column(Integer, nullable=True) 
    database_id = Column(Integer, ForeignKey(DatabasesOnInstance.id), nullable=True)
    schema_id = Column(Integer, ForeignKey(SchemaOnInstance.id), nullable=True)

    # Relationships
    databases_on_instance = relationship("DatabasesOnInstance")
    schema_on_instance = relationship("SchemaOnInstance")

    def __repr__(self):
        return "<ParametersInSchemas({})>".format(self.id)

Base.metadata.create_all(engine)

