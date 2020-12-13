import pandas
from snowflake.connector.pandas_tools import pd_writer

class LoadData():

    def __init__(self, engine):

        self.engine = engine

    def dump_data(self, table_name, dataframe):

        # Write the data from the DataFrame to the table named in table_name agument.
        dataframe.columns = map(lambda x : str(x).upper(), dataframe.columns)

        #insert df into sfo's database table
        dataframe.to_sql(table_name, self.engine, index=False, method=pd_writer, if_exists="append")

        return True