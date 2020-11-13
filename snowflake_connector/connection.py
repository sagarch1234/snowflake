#!/usr/bin/env python
import snowflake.connector
import logging
from rest_framework import status


logger = logging.getLogger(__name__)

logging.basicConfig(
    filename='/tmp/snowflake_python_connector.log',
    level=logging.INFO)


def connect_snowflake_instance(user, password, account):

    try:
        connection = snowflake.connector.connect(user=user, password=password, account=account, role='ACCOUNTADMIN')
    
    except Exception as error_message:

        return {
            "error_no" : error_message.errno,
            "error_message" : error_message.raw_msg,
            "status" : status.HTTP_400_BAD_REQUEST
        }
        
    return {
        "connection_object" : connection,
        "message" : "Connection successful.",
        "status" : status.HTTP_200_OK
    }
     

# connection = connect_snowflake_instance(user='jeet', password='Jeet@123', account='fp43891.us-central1.gcp')

# print(connection['connection_object'].account)

# cs = ctx.cursor()

# try:
#     cs.execute("SELECT current_version()")
#     one_row = cs.fetchone()
#     print(one_row[0])
# finally:
#     cs.close()
#     ctx.close()


# try:
#     cs.execute("SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_LOAD_HISTORY;")
#     one_row = cs.fetchone()
#     print(one_row)
# finally:
#     cs.close()
#     ctx.close()

# ctx = snowflake.connector.connect(
#     user='jeet',
#     password='Jeet@123',
#     account='fp43891.us-central1.gcp'
#     )

# con = snowflake.connector.connect(
#     user='jeet99',
#     password='Jeet@123',
#     account='hk06174.us-central1.gcp'
#     )

# print(ctx.messages)
# print(ctx.errors)
# print(ctx)