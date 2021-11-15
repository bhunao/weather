import requests

from datetime import datetime

from pprint import pprint

import schemas

def get_data(city: str) -> schemas.Model:
    KEY = "dc0f09091ff236e4d77bbba9310879ec"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}"
    response = requests.get(URL)
    return response.json()

def transform_data(data: schemas.Model) -> schemas.Weather:
    if data.get("main")  is None:
        return {"message": "sum ting wong"}
    output = dict()
    output['now'] = datetime.now()
    output['min'] = data.get('main').get('temp_min')
    output['max'] = data.get('main').get('temp_max')
    output['avg'] = data.get('main').get('temp')
    output['feels_like'] = data.get('main').get('feels_like')

    city = dict()
    city['name'] = data.get('name')
    city['country'] = data.get('sys').get('country')

    output['city'] = city
    return output
