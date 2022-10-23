import scrapy

from scrapy import Selector


def clear_link_array(link_arr: list[str]) -> list[str]:
    cleared_array = []
    for index, text in enumerate(link_arr):
        if text.__contains__("/wiki"):
            newt = text.replace("/wiki/", "")
            cleared_array.append(newt)

    return cleared_array


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["wikipedia.org"]

    def __init__(self, *args, **kwargs):
        super(ExampleSpider, self).__init__(*args, **kwargs)

        date = kwargs.get("date")
        if not date:
            raise ValueError("No date given")

        self.start_urls = [f"https://en.wikipedia.org/wiki/{date}"]

    def parse(self, response):

        sections = response.css(".mw-parser-output ul")[4:13]

        list_of_lists: list[list[str]] = []

        for section in sections:
            events = section.css("li")
            for event in events:
                result: Selector = event.css("a::attr(href)")
                link_array = result.extract()

                cleared_link_array = clear_link_array(link_array)
                list_of_lists.append(cleared_link_array)

        yield {"links": list_of_lists}
