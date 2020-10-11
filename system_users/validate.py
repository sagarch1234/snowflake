#!/usr/bin/env python
import snowflake.connector

    
ctx = snowflake.connector.connect(
    user='jeet',
    password='Jeet@123',
    account='fp43891.us-central1.gcp',
    role='ACCOUNTADMIN'
    )

cs = ctx.cursor()

# try:
#     cs.execute("SELECT current_version()")
#     one_row = cs.fetchone()
#     print(one_row[0])
# finally:
#     cs.close()
#     ctx.close()


try:
    cs.execute("SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_LOAD_HISTORY;")
    one_row = cs.fetchone()
    print(one_row)
finally:
    cs.close()
    ctx.close()

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

# print(ctx)
# print(con)