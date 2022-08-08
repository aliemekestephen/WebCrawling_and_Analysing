from Event_record import EventRecord
from Database_Transactions import DatabaseTransaction
from charts import Plot


MENU_PROMPT = """
    Please enter 
    'C' to crawl and display database,
    'S' to save crawled data to databases,
    'D' to display saved date from database,
    'P' to plot number of events in a day,
    'Q' to quit.
    """


class AppRun:

    @staticmethod
    def app_menu():
        user_options = {
            'c': EventRecord().event_data,
            's': DatabaseTransaction().insert_data,
            'd': DatabaseTransaction().read_database,
            'p': Plot().plot_data
        }

        selection = input(MENU_PROMPT).lower()
        while selection != 'q':
            if selection in user_options:
                selected_option = user_options[selection]
                result = selected_option()
                print(result)
            else:
                print('invalid command. Please try again')

            selection = input(MENU_PROMPT).lower()


AppRun().app_menu()  # TODO Improve the app



