from datetime import date
from weather.config.config_reader import config

from urllib import request
import requests

from .currentWeather import CurrentWeather
from .models import Forecast


API_CURRENTWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
API_FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"


def get_current_weather(lat: float, log: float) -> CurrentWeather:
    params = {"lat": lat, "lon": log, "appid": config.weather_apikey}
    r = requests.get(API_CURRENTWEATHER_URL, params=params)
    weather = CurrentWeather.parse_raw(r.text)

    return weather


def get_forecast(lat: float, log: float, date: date = "2022-10-18") -> Forecast:
    params = {"lat": lat, "lon": log, "appid": config.weather_apikey}
    r = requests.get(API_FORECAST_URL, params=params)
    forecast = Forecast.parse_raw(r.text)

    forecast.choose_date(date)
    return forecast


# curr = get_current_weather(44.34, 10.99)
# forecast = get_forecast(44.34, 10.99, date(2022, 10, 19))

# print([elem.dt_txt for elem in forecast.list])
