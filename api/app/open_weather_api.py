import requests

from . import schemas, endpoint, key


def get_data(city: str, endpoint, key) -> schemas.Model:
    URL = endpoint.format(city=city, key=key)
    response = requests.get(URL)
    return response.json()

def transform_data(data: schemas.Model) -> schemas.Weather:
    if data.get("main")  is None:
        return "error"
    output = dict()
    output['min'] = data.get('main').get('temp_min')
    output['max'] = data.get('main').get('temp_max')
    output['avg'] = data.get('main').get('temp')
    output['feels_like'] = data.get('main').get('feels_like')

    city = dict()
    city['name'] = data.get('name')
    city['country'] = data.get('sys').get('country')

    output['city'] = city
    return output
