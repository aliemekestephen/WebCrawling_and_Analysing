from bs4 import BeautifulSoup

from Locators.all_events_locator import AllEventLocators
from Parsers.Events_Parser import ParsedEvent


class AllEventsPage:
    """
    Takes in the URL to be scraped,
    Calls the ParsedEvent() class from Events_Parser
    Returns a list of unprocessed web page scrapings
    """

    def __init__(self, page_url):

        self.soup = BeautifulSoup(page_url, 'html.parser')

    @property
    def events(self):
        return [ParsedEvent(e) for e in self.soup.select(AllEventLocators.EVENTS)]