from fastapi import FastAPI

from .main import get_forecast
from .models import Forecast


weatherapi = FastAPI()


@weatherapi.get(
    "/forecast",
    response_model=Forecast,
    description="Insert date in 2022-10-20 format",
)
async def getForecast(lat: float = 44.34, log: float = 10.99, date: str = "2022-10-20"):
    forc = get_forecast(lat, log, date)
    return forc
