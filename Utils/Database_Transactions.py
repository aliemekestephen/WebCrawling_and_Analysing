from Utils.Database_Connection import DatabaseConnection


class DatabaseTransaction:

    @staticmethod
    def create_table():
        with DatabaseConnection() as cursor:
            create_table = """CREATE TABLE IF NOT EXISTS crawled_event_data (
                                                    No              int PRIMARY KEY,
                                                    title           varchar(150) NOT NULL,
                                                    venue           varchar(50),
                                                    date            date,
                                                    time            time,
                                                    artist          varchar(40),
                                                    artist_works    varchar(60),
                                                    image_link      varchar(256)
                                                    )

                                """
            cursor.execute(create_table)

    def insert_data(self):
        pass


DatabaseTransaction.create_table()
