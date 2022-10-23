#  Use pydantic to read .env config instead of self-written parser
from pydantic import BaseSettings


class Settings(BaseSettings):
    # Weather service
    weather_apikey: str

    class Config:
        env_file = "./weather/config/file.env"
        env_file_encoding = "utf-8"


config = Settings()
