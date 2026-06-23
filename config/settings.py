from pydantic_settings import BaseSettings
from typing import Literal

class Settings(BaseSettings):
    app_name: str = "Truck & Roll"
    architecture_mode: Literal["mvc", "mvvm", "both"] = "both"

settings = Settings()
