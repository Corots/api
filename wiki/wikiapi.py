from fastapi import FastAPI

from wiki.models import DayEvents
from wiki.methods import get_full_list, get_list_by_day


app = FastAPI()


# Method to get all events it the year
# @app.get("/getAllEvents", response_model=list[DayEvents])
# def getEvents():
#     return get_full_list()


@app.get("/getEventsByDay", response_model=DayEvents)
def getEvents(date: str = "January_1"):
    return get_list_by_day(date)
