import pandas
import os
from snowflake.connector.pandas_tools import pd_writer

class LoadData():

    def __init__(self, engine, connection):

        self.engine = engine
        self.connection = connection
    
    def get_last_id(self, table_name):

        con = self.connection['connection_object']
                
        schema = str(os.environ.get('SCHEMA_NAME_PARAMS'))
        database = str(os.environ.get('SNOWFLAKE_DATABASE_NAME'))
        table_name = str(table_name.upper())

        sql = 'SELECT max(ID) AS max_ID FROM' + ' ' + database + '.' + schema + '.' + table_name;
        
        try:
            
            id = con.execute(sql).fetchone()

        except Exception as identifier:

            id=0

            return id

        if id[0] is None:

            id = 0
            
            return id

        return id[0]

    def dump_data(self, table_name, dataframe, index_label):

        dataframe.columns = dataframe.columns.str.upper()

        id = self.get_last_id(table_name=table_name)
        
        dataframe.index = range(id+1, len(dataframe)+id+1)

        # insert df into snowflake database tables.
        dataframe.to_sql(table_name, self.engine, index=True, index_label=index_label, method=pd_writer, if_exists="append")

        return True