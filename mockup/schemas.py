from typing import List
from pydantic import BaseModel


class City(BaseModel):
    name: str
    country: str


class Weather(BaseModel):
    min: float
    max: float
    avg: float
    feels_like: float
    city: City

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
    pressure: int
    humidity: int
    temp_min: float
    temp_max: float


class Wind(BaseModel):
    speed: float
    deg: int


class Clouds(BaseModel):
    all: int


class Sys(BaseModel):
    type: int
    id: int
    message: float
    country: str
    sunrise: int
    sunset: int


class Model(BaseModel):
    coord: Coord
    weather: List[WeatherItem]
    base: str
    main: Main
    visibility: int
    wind: Wind
    clouds: Clouds
    dt: int
    sys: Sys
    id: int
    name: str
    cod: int
