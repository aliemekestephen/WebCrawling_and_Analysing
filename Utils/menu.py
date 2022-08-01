from app import events


class EventRecord:
    """
    Receives event data from the app
    Returns processed data in a list containing tuples
    """

    def __init__(self):
        self.events = events

    def event_data(self) -> list:
        event_entry_list = []

        for event in self.events:
            event_string = str(event)
            event_entry_list.append(tuple(event_string.split(' : ')))
        return event_entry_list


# EventRecord().event_data() # TODO always remove before final
