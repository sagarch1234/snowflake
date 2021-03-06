import sys
import pandas as pd
import os
import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)


class GetCustomerData():

    def __init__(self, engine):

        self.engine = engine

    def get_data(self, sql):

        df = pd.read_sql_query(sql, self.engine)

        return df