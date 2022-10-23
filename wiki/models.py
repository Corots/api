from pydantic import BaseModel, Field
from enum import Enum

months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}


class DataType(Enum):
    event = "Events"
    birth = "Births"
    death = "Deaths"


class AbsEvent(BaseModel):
    description: str
    date: str
    linked_articles: list[str]


class Event(AbsEvent):
    pass


class Birth(AbsEvent):
    pass


class Death(AbsEvent):
    pass


# class Link(BaseModel):
#     link: list[str]


class LinkList(BaseModel):
    links: list[list[str]]


class DayEvents(BaseModel):
    events: list[Event]
    births: list[Birth]
    deaths: list[Death]

    def set_links(self, link_list: list[list[str]]):

        all_events: list[AbsEvent] = self.events + self.births + self.deaths

        try:
            for event in all_events:
                event.linked_articles = link_list.pop(0)
        except IndexError:
            print("list os over before the end of events")
