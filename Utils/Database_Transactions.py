from Utils.Database_Connection import DatabaseConnection
from Utils.menu import EventRecord


class DatabaseTransaction:
    """
    creates cursor from the Database Connection
    Manages all transactions to the Database
    """

    @staticmethod
    def create_table():
        with DatabaseConnection() as cursor:
            create_table = """CREATE TABLE IF NOT EXISTS crawled_event_data (
                                                    _id             serial PRIMARY KEY,
                                                    title           varchar,
                                                    venue           varchar,
                                                    date            date,
                                                    time       time,
                                                    artist          varchar,
                                                    artist_works    varchar,
                                                    image_link      varchar
                                                    )

                                """
            cursor.execute(create_table)
            print('Table created successfully')

    @staticmethod
    def insert_data():
        with DatabaseConnection() as cursor:

            insert_script = 'INSERT INTO crawled_event_data (title, venue, date, time, artist, artist_works, ' \
                                                            'image_link) ' \
                            'VALUES (%s, %s, %s, %s, %s, %s, %s)'
            insert_values = EventRecord().event_data()

            for item in insert_values:
                cursor.execute(insert_script, item)

    @staticmethod
    def read_data():
        data_dict = dict()
        all_data_list = []
        with DatabaseConnection() as cursor:
            cursor.execute('SELECT * FROM crawled_event_data')
            for record in cursor.fetchall():
                data_dict['title'] = record['title']
                data_dict['venue'] = record['venue']
                data_dict['date'] = record['date']
                data_dict['time'] = record['time']
                data_dict['artist'] = record['artist']
                all_data_list.append(data_dict)
                data_dict = {}

        return all_data_list


DatabaseTransaction.read_data()
