import pandas as pd

from events import events


class EventRecord:
    """
    Receives event data from the app
    Returns processed data in a DataFrame
    """

    def __init__(self):
        self.events = events
        self.event_entry_list = []

    def event_data(self) -> pd.DataFrame:
        for event in self.events:
            event_string = str(event)
            self.event_entry_list.append(tuple(event_string.split(' : ')))

        event_df = pd.DataFrame(self.event_entry_list, columns=['title', 'venue', 'date', 'time', 'artist',
                                                                'artist_programs', 'image_link'])
        return event_df
