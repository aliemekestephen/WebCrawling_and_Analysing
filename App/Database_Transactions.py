from collections import Counter

import pandas as pd

from sqlalchemy import (Table, MetaData, Column, Integer, String, Date, Time)

from Database_Connection import DatabaseConnection
from Event_record import EventRecord


class DatabaseTransaction:
    """
    creates cursor from the Database Connection
    Manages all transactions to the Database
    """

    def __init__(self):
        self.all_data_list = None

    @staticmethod
    def create_table():
        with DatabaseConnection() as engine:

            meta_data = MetaData()
            table = Table('crawled_event_data', meta_data,
                            Column('index', Integer(), primary_key=True),
                            Column('title', String(200)),
                            Column('venue', String(200)),
                            Column('date', Date()),
                            Column('time', Time()),
                            Column('artist', String(200)),
                            Column('artist_programs', String(200)),
                            Column('image_link', String())
                          )
            try:
                meta_data.create_all(engine)
                print(f'Table {table} created successfully')
            except Exception as error:
                print(f'The following error occurred!: \n\n{error}')

    def insert_data(self):
        self.create_table()  # TODO check password request maybe create at runtime? event_data()
        df = EventRecord().event_data()
        with DatabaseConnection() as engine:
            try:
                df.to_sql('crawled_event_data', engine, if_exists='append', index=True)
                return print('data inserted successfully!')
            except Exception as error:
                print(f'The following error occurred!: \n\n{error}')

    @staticmethod
    def read_database():
        with DatabaseConnection() as engine:
            try:
                dataframe = pd.read_sql('crawled_event_data', engine)
                return dataframe
            except Exception as error:
                print('Data base is empty or the following error occured: \n\n{error}')

    def convert_data(self):  # Converts the event occurrence into a list
        month = int(input('Please enter month in integer: '))
        event_list = []
        df = self.read_database()
        records = df.values.tolist()
        for record in records:
            if record[3].month == month:
                event_list.append(record[3].day)

        count = Counter(event_list)
        y_axis = list(count.values())
        x_axis = list(count.keys())
        plot_data = zip(x_axis, y_axis)
        return list(plot_data)
