import requests

from all_events_page import AllEventsPage

page_content = requests.get('https://www.lucernefestival.ch/en/program/summer-festival-22').content
page = AllEventsPage(page_content)

out = []
events = page.events
