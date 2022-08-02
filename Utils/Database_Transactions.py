import numpy as np

from collections import Counter
from Utils.Database_Connection import DatabaseConnection
from Utils.menu import EventRecord


class DatabaseTransaction:
    """
    creates cursor from the Database Connection
    Manages all transactions to the Database
    """

    def __init__(self):
        self.all_data_list = None

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
            print('Data inserted successfully')

    def read_data(self):
        data_dict = dict()
        self.all_data_list = []
        with DatabaseConnection() as cursor:
            cursor.execute('SELECT * FROM crawled_event_data')
            for record in cursor.fetchall():
                data_dict['title'] = record['title']
                data_dict['venue'] = record['venue']
                data_dict['date'] = record['date']
                data_dict['time'] = record['time']
                data_dict['artist'] = record['artist']
                self.all_data_list.append(data_dict)
                data_dict = {}

        return self.all_data_list

    def convert_data(self):  # Converts the event occurrence into numpy
        month = int(input('Please enter month in integer: '))
        event_list = []
        records = self.read_data()
        for record in records:
            if record['date'].month == month:
                event_list.append(record['date'].day)

        count = Counter(event_list)
        y_axis = list(count.values())
        x_axis = list(count.keys())

        return y_axis, x_axis


# DatabaseTransaction().convert_data() # TODO remove
