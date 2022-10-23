from __future__ import annotations
from datetime import date
import datetime

from typing import List, Optional

from pydantic import BaseModel, Field


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    sea_level: int
    grnd_level: int
    humidity: int
    temp_kf: float


class WeatherItem(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Clouds(BaseModel):
    all: int


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float


class Sys(BaseModel):
    pod: str


class Rain(BaseModel):
    field_3h: float = Field(..., alias="3h")


class ListItem(BaseModel):
    dt: int
    main: Main
    weather: List[WeatherItem]
    clouds: Clouds
    wind: Wind
    visibility: int
    pop: float
    sys: Sys
    dt_txt: str
    rain: Optional[Rain] = None


class Coord(BaseModel):
    lat: float
    lon: float


class City(BaseModel):
    id: int
    name: str
    coord: Coord
    country: str
    population: int
    timezone: int
    sunrise: int
    sunset: int


class Forecast(BaseModel):
    cod: Optional[str] = None
    message: Optional[int] = None
    cnt: Optional[int] = None
    list: Optional[List[ListItem]] = None
    city: Optional[City] = None

    def choose_date(self, date: str):
        new_list = []
        for elem in self.list:

            elem_date = datetime.datetime.strptime(elem.dt_txt, "%Y-%m-%d %H:%M:%S")
            choosen_date = datetime.datetime.strptime(date, "%Y-%m-%d")
            if elem_date.date() == choosen_date.date():
                new_list.append(elem)

        self.list = new_list
