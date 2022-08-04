class EventLocators:
    """
    Locators for an item in the HTML page.

    Contains elements that will be searched.
    """

    TITLE_LOCATOR = 'div.event-content div.event-text.cell.auto.grow p.event-title.h3 a'  # good to go
    VENUE_LOCATOR = 'div.cell.xlarge-6.body-small'
    DATE_LOCATOR = 'div.cell.xlarge-6.body-small'
    TIME_LOCATOR = 'div.cell.xlarge-6.body-small'
    ARTIST_LOCATOR = 'div.event-content div.event-text.cell.auto.grow p.event-title.h3 a'
    ARTIST_WORKS_LOCATOR = 'div.cell.xlarge-6.body-small'
    IMAGE_LINK_LOCATORS = 'div.cell.shrink.show-for-large a figure picture source'
