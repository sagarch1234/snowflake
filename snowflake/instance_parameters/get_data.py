import sys
import pandas as pd
import os
import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)


class GetCustomerData():

    def __init__(self, engine):

        self.engine = engine

    def get_data(self, sql, database_name = None, database_schema = None):

        if (database_name is None)  or (database_schema is None):
            df = pd.read_sql_query(sql, self.engine)

        elif(database_name is not None) and (database_schema is None):
            sql = sql.format(database_name)
            df = pd.read_sql_query(sql, self.engine)

        else:
            sql = sql.format(database_name, database_schema)
            df = pd.read_sql_query(sql, self.engine)
        
        return df