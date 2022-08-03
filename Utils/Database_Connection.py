from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


class DatabaseConnection:
    """
    Context Manager Class
    Creates the connection to the Database
    Manages the commit
    Closes the Database connection
    """

    def __init__(self):
        self.engine = None

    def __enter__(self):
        # password = input('Please enter Postgres password: ')

        try:
            url = f'postgresql://postgres:1Thesaint@127.0.0.1:5432/Data_Hive'
            print('checking if database exists...')
            if not database_exists(url):
                print('Database not found! Creating database...')
                create_database(url)
            print('connecting to database...')
            self.engine = create_engine(url, pool_size=50, echo=False)
            print('Connection established.')
            return self.engine
        except Exception as error:
            print(error)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print('Connection terminated')

    # def get_engine_from_credentials(self):
    #     keys = ['user', 'host', 'passwd', 'port', 'database']
    #     if not all(key in keys for key in credentials.keys()):
    #         raise Exception ('Bad credentials...')
    #
    #     return self.get_engine(credentials['user'],
    #                            credentials['host'],
    #                            credentials['passwd'],
    #                            credentials['port'],
    #                            credentials['database'])


# DatabaseConnection().get_engine_from_credentials() #TODO remove before final

    # def __enter__(self):
    #     # password = input('Please enter Postgres password: ')
    #
    #     try:
    #         print('Connecting to the database...')
    #         self.connection = psycopg2.connect(
    #             host='127.0.0.1',
    #             database='Data_Hive',
    #             user='postgres',
    #             password='1Thesaint',
    #             port='5432'
    #         )
    #         cursor = self.connection.cursor()
    #         print('Connection successful')
    #         return cursor
    #     except Exception as error:
    #         print(error)
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     if exc_type or exc_val or exc_tb:
    #         self.connection.close()
    #     self.connection.commit()
    #     self.connection.close()
    #     print('Connection terminated')


