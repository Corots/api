from fastapi import FastAPI
import weather.weatherapi as weatherapi
import wiki.wikiapi as wikiapi

app = FastAPI()
app.mount("/weather", weatherapi.weatherapi)
app.mount("/wiki", wikiapi.app)
