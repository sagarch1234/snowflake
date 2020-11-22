import sys

sys.path.insert(1,  '/snowflake-backend/snowflake/instance_connector')

from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column, Text, Boolean, ForeignKey, create_engine, Time, Binary
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
    __tablename__ = 'account_parametes'
    __table_args__ = {
        'extend_existing' : True,
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, primary_key=True)
    key = Column(String(200))
    value = Column(String(200))
    default = Column(String(200))
    level = Column(String(200))
    description = Column(Text)
    type = Column(String(100))
    instance_id = Column(Integer) 

    def __repr__(self):
        return "<AccountParameters({})>".format(self.id)
    

class DatabasesOnInstance(Base):
    '''
    '''
    __tablename__ = 'databases_on_instance'
    __table_args__ = {
        'extend_existing' : True,
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, primary_key=True)
    created_on = Column(Time)
    name = Column(String(100))
    is_default = Column(Binary())
    is_current = Column(Binary())
    origin = Column(String(200))
    owner = Column(String(100))
    comment = Column(Text)
    options = Column(String(100))
    retention_time = Column(Integer)
    instance_id = Column(Integer)

    def __repr__(self):
        return "<DatabasesOnInstance({})>".format(self.id)


class SchemaOnInstance(Base):
    '''
    '''
    __tablename__ = 'schema_on_instance'
    __table_args__ = {
        'extend_existing' : True,
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, primary_key=True)
    created_on = Column(Time)
    name = Column(String(100))
    is_default = Column(Binary())
    is_current = Column(Binary())
    database_name = Column(String(200))
    owner = Column(String(100))
    comment = Column(Text)
    options = Column(String(100))
    retention_time = Column(Integer)
    instance_id = Column(Integer)

    def __repr__(self):
        return "<SchemaOnInstance({})>".format(self.id)


class ParametersInDatabase(Base):
    '''
    '''
    __tablename__ = 'parameters_in_database'
    __table_args__ = {
        'extend_existing' : True,
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, primary_key=True)
    key = Column(String(200))
    value = Column(String(200))
    default = Column(String(200))
    level = Column(String(200))
    description = Column(Text)
    type = Column(String(100))
    instance_id = Column(Integer) 
    database_id = Column(Integer, ForeignKey(DatabasesOnInstance.id))

    # Relationships
    databases_on_instance = relationship("DatabasesOnInstance")

    def __repr__(self):
        return "<ParametersInDatabase({})>".format(self.id)


class ParametersInSchemas(Base):
    '''
    '''
    __tablename__ = 'parameters_in_schemas'
    __table_args__ = {
        'extend_existing' : True,
        'schema' : 'SFOPT_TEST_SCHEMA'
    }

    id = Column(Integer, primary_key=True)
    key = Column(String(200))
    value = Column(String(200))
    default = Column(String(200))
    level = Column(String(200))
    description = Column(Text)
    type = Column(String(100))
    instance_id = Column(Integer) 
    database_id = Column(Integer, ForeignKey(DatabasesOnInstance.id))
    schema_id = Column(Integer, ForeignKey(SchemaOnInstance.id))

    # Relationships
    databases_on_instance = relationship("DatabasesOnInstance")
    schema_on_instance = relationship("SchemaOnInstance")

    def __repr__(self):
        return "<ParametersInSchemas({})>".format(self.id)


Base.metadata.create_all(engine)

