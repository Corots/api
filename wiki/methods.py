from multiprocessing import Process
import os
import wikipediaapi
from wikipediaapi import WikipediaPageSection

from wiki.models import (
    AbsEvent,
    DataType,
    Event,
    Birth,
    Death,
    DayEvents,
    LinkList,
    months,
)
import datetime

from scrapy.crawler import CrawlerProcess
from scraper.scraper.spiders.example import ExampleSpider


import json
from wiki.models import LinkList


def crawl(name: str, date: str):
    crawler = CrawlerProcess(
        settings={
            "FEEDS": {
                name: {"format": "json"},
            },
        }
    )
    crawler.crawl(ExampleSpider, date=date)
    crawler.start()


def gen_name(count: int):
    # {datetime.datetime.now()}
    return f"myfile{count}.json"


def update_links(dayEvent: DayEvents, filename: str):

    aList: list[dict] = json.load(open(filename))
    obj = LinkList.parse_obj(aList[0])
    dayEvent.set_links(obj.links)


def create_absevents(
    date: str, sections: list[WikipediaPageSection], type: DataType
) -> list[AbsEvent]:

    absEvents_list: list[AbsEvent] = []
    for section in sections:

        for absevent in section.text.split("\n"):

            text = absevent.split("–")[-1].strip()
            year = absevent.split("–")[0].strip()

            # date_text = f"{date.replace('_', '–')}"
            print(date)
            date_text_edited = datetime.datetime.strptime(date, "%B_%d").strftime(
                "%m/%d/"
            )

            abs_dict_event = {
                "description": text,
                "date": date_text_edited + year,
                "linked_articles": [],
            }

            if type == DataType.event:
                absEvents_list.append(Event.parse_obj(abs_dict_event))

            if type == DataType.birth:
                absEvents_list.append(Birth.parse_obj(abs_dict_event))

            if type == DataType.death:
                absEvents_list.append(Death.parse_obj(abs_dict_event))

    return absEvents_list


def print_sections(date: str, sections: list[WikipediaPageSection]):

    events = []
    births = []
    deaths = []

    # check every section (event, birth, death)
    for s in sections:

        print(s.title)
        if s.title == DataType.event.value:
            events = create_absevents(date, s.sections, DataType.event)
        elif s.title == DataType.birth.value:
            births = create_absevents(date, s.sections, DataType.birth)
        elif s.title == DataType.death.value:
            deaths = create_absevents(date, s.sections, DataType.death)

    dayEvents = DayEvents(events=events, births=births, deaths=deaths)
    return dayEvents


def get_full_list() -> list[DayEvents]:

    full_list_events: list[DayEvents] = []

    for month, num_day in zip(months, months.values()):
        for day in range(1, num_day + 1):
            wiki_wiki = wikipediaapi.Wikipedia(
                language="en", extract_format=wikipediaapi.ExtractFormat.WIKI
            )
            page_py = wiki_wiki.page(f"{month}_{day}")
            dayEvent = print_sections(f"{month}_{day}", page_py.sections)

            full_list_events.append(dayEvent)

    return full_list_events


def delete_file(path: str):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file does not exist")


def get_list_by_day(date: str):
    wiki_wiki = wikipediaapi.Wikipedia(
        language="en", extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    page_py = wiki_wiki.page(date)
    dayEvent = print_sections(date, page_py.sections)

    name = gen_name(4)
    process = Process(target=crawl, args=(name, date))
    process.start()
    process.join()

    update_links(dayEvent, name)
    delete_file(name)

    return dayEvent
