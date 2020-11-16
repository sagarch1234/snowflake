import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level = logging.INFO)


class RecordParameters():
    '''
    '''
    def __init__(self, connection):
        self.connection = connection

    def account_level(self):

        logging.info("Collecting account's parameters from customer's instance.")

        results = self.connection.execute('show parameters in account').fetchall()

        return results

    def get_databases(self):

        logging.info("Geting list of databases form customer's instance.")

        results = self.connection.execute('show databases').fetchall()

        return results

    def database_level(self):

        logging.info("Getting parameters of each database from customer's instance.")

        databases = self.get_databases()

        for database in databases:

            result = self.connection.execute('show parameters in DATABASE' + ' ' + database['name']).fetchall()
            
            return result
            
    def schema_level(self):
        pass