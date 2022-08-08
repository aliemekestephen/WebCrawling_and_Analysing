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
        try:
            url = f'postgresql://postgres:1Thesaint@172.18.0.2:5432/Data_Hive' #  use localhost when connecting locally
            print('checking if database exists...')
            if not database_exists(url):
                print('Database not found! Creating database...')
                create_database(url)
            print('connecting to database...')
            self.engine = create_engine(url)
            print('Connection established.')
            return self.engine
        except Exception as error:
            print(error)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print('Connection terminated')
