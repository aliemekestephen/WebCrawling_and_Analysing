import re
from datetime import datetime

from event_locator import EventLocators


class ParsedEvent:
    """
    This class takes in an HTML page from the parent.
    Returns the properties of the item in its.
    """

    def __init__(self, parent):
        self.parent_soup = parent

    def __repr__(self):
        return f'{self.title()} : {self.venue()} : {self.date()[0]} : {self.date()[1]}' \
               f' : {self.artist()} : {self.artist_works()} : {self.image_link()}'

    def title(self):
        locator = EventLocators.TITLE_LOCATOR
        event_title = self.parent_soup.select_one(locator)
        return event_title.get_text().split('|')[0].strip(' ')

    def venue(self):
        locator = EventLocators.VENUE_LOCATOR
        pattern = '\| [a-zA-Z]+.+'
        event_venue_item = self.parent_soup.select_one(locator)
        event_venue = re.search(pattern, str(event_venue_item)).group().strip('| ')
        return event_venue

    def date(self):
        locator = EventLocators.DATE_LOCATOR
        pattern = '([a-zA-Z]{3}) ([0-9]+)\.([0-9]+)'
        event_date_item = self.parent_soup.select_one(locator)
        event_day = re.search(pattern, str(event_date_item)).group(2)
        event_month = re.search(pattern, str(event_date_item)).group(3)
        date = datetime(2022, int(event_month), int(event_day), int(self.time()[0]), int(self.time()[1]))
        return date.date(), date.time()

    def time(self):
        locator = EventLocators.TIME_LOCATOR
        pattern = '([0-9]+\.[0-9]+)\. \| ([0-9]+\.[0-9]+)'
        event_time_item = self.parent_soup.select_one(locator)
        event_time = re.search(pattern, str(event_time_item)).group(2).split('.')
        return event_time

    def artist(self):
        locator = EventLocators.TITLE_LOCATOR
        event_title = self.parent_soup.select_one(locator)
        return event_title.get_text().split(' | ')[1:]

    def artist_works(self):
        locator = EventLocators.ARTIST_WORKS_LOCATOR
        pattern = '[a-zA-Z]+ +\| [a-zA-Z]+.+'

        event_artist_works_item = self.parent_soup.select(locator)[1]
        try:
            re.search(pattern, str(event_artist_works_item)).group()
        except AttributeError:
            return []
        event_artist_works = re.search(pattern, str(event_artist_works_item)).group().split(' | ')
        return event_artist_works

    def image_link(self):
        url_link = 'www.lucernefestival.ch'
        locator = EventLocators.IMAGE_LINK_LOCATORS
        event_image = self.parent_soup.select_one(locator).attrs['srcset']
        return url_link+event_image

