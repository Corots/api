from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Coord(BaseModel):
    lon: float
    lat: float


class WeatherItem(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float


class Clouds(BaseModel):
    all: int


class Sys(BaseModel):
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int


class CurrentWeather(BaseModel):
    coord: Optional[Coord] = None
    weather: Optional[List[WeatherItem]] = None
    base: Optional[str] = None
    main: Optional[Main] = None
    visibility: Optional[int] = None
    wind: Optional[Wind] = None
    clouds: Optional[Clouds] = None
    dt: Optional[int] = None
    sys: Optional[Sys] = None
    timezone: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None
    cod: Optional[int] = None
