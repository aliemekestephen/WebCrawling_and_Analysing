import psycopg2.extras  # to read as dictionary


class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        password = input('Please enter Postgres password: ')

        try:
            self.connection = psycopg2.connect(
                host='127.0.0.1',
                database='Data_Hive',
                user='postgres',
                password=password,
                port='5432'
            )
            cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
            return cursor
        except Exception as error:
            print(error)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        self.connection.commit()
        self.connection.close()
