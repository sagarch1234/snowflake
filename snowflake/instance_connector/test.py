import connection.SnowflakeConnector
print("here")

con = SnowflakeConnector('jeet', 'Jeet@123', 'fp43891.us-central1.gcp')
print(con.connect_snowflake_instance)


