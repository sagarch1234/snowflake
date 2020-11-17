from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.delarative import declarative_base

from snowflake.instance_connector.connection import SnowflakeConnector

import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)

connection = SnowflakeConnector('shivkant', 'Shiva@123!!*', 'lt90919.us-central1.gcp')

engine = connection.get_engine()

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

class AccountParameters(Base):
    '''
    '''
    __tablename__ = 'account_parametes'

    id = Column(Integer, primary_key=True)
    key = Column(String(200))
    value = Column(String(200))
    default = Column(String(200))
    level = Column(String(200))
    description = Column(Text)
    type = Column(String(100))
    instance = Column(Integer) 


class DatabasesOnInstance(Base):
    '''
    '''
    __tablename__ = 'databases_on_instance'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    is_default = Column(Boolean)
    is_current = Column(Boolean)
    origin = Column(String(200))
    owner = Column(String(100))
    comment = Column(Text)
    options = Column(String(100))
    retention_time = Column(Integer)
    instance = Column(Integer)


class SchemaOnInstance(Base):
    '''
    '''
    __tablename__ = 'schema_on_instance'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    is_default = Column(Boolean)
    is_current = Column(Boolean)
    database_name = Column(String(200))
    owner = Column(String(100))
    comment = Column(Text)
    options = Column(String(100))
    retention_time = Column(Integer)
    instance = Column(Integer)


class ParametersInDatabase(Base):
    '''
    '''
    __tablename__ = 'parameters_in_database'

    id = Column(Integer, primary_key=True)
    key = Column(String(200))
    value = Column(String(200))
    default = Column(String(200))
    level = Column(String(200))
    description = Column(Text)
    type = Column(String(100))
    instance = Column(Integer) 
    database = Column(Integer, ForeignKey('databases_on_instance.id'))

class ParametersInSchemas(Base):
    '''
    '''
    __tablename__ = 'parameters_in_database'

    id = Column(Integer, primary_key=True)
    key = Column(String(200))
    value = Column(String(200))
    default = Column(String(200))
    level = Column(String(200))
    description = Column(Text)
    type = Column(String(100))
    instance = Column(Integer) 
    database = Column(Integer, ForeignKey('databases_on_instance.id'))
    schema = Column(Integer, ForeignKey('schema_on_instance.id'))
    

Base.metadata.create_all(engine)