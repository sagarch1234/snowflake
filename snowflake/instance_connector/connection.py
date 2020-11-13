from sqlalchemy import create_engine
import status



class SnowflakeConnector:

    def __init__(self, user, password, account, role):
        self.user = user
        self.password = password
        self.account = account
        self.role = role
        # self.snowflake_instance = snowflake_instance
    
    def connect_snowflake_instance(self):

        engine = create_engine(
            'snowflake://{user}:{password}@{account}/?{role}='.format(
                user=self.user,
                password=self.password,
                account=self.account,
                role=self.role
            )
        )

        try:

            connection = engine.connect()
            # results = connection.execute('select current_version()').fetchall()
            # print(results[0])
        
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
