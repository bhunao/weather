import open_weather_api
import schemas

from flask import Flask, json
from flask_caching import Cache
from cache import My_Cache

config = {
        "DEBUG": True,
        "CACHE_TYPE": "SimpleCache",
        "CACHE_DEFAULT_TIMEOUT": 300
        }

cached_keys = []


api = Flask(__name__)
api.config.from_mapping(config)
cache = Cache(api)
mycache = My_Cache(cache)

@api.route('/weather/<city>', methods=['GET'])
# @cache.memoize(50)
def get_city_weather(city: str):
    data = open_weather_api.get_data(city)
    result = open_weather_api.transform_data(data)
    c = cache.cache.get(city)
    if c:
        return json.dumps(c)
    else:
        cache.cache.set(city, result, timeout=30)
        cached_keys.append(city)
        return json.dumps(result)

@api.route('/w/<city>', methods=['GET'])
def get_w(city: str):
    result = mycache.get(city)
    if result is None:
        data = open_weather_api.get_data(city)
        result = open_weather_api.transform_data(data)
        mycache.set(city, result)
        return json.dumps(result)
    return json.dumps(result)

@api.route('/w', methods=['GET'])
def get_all_w():
    keys = mycache.keys
    r = {k: mycache.get(k) for k in keys}
    return json.dumps(r)
    

@api.route('/weather', methods=['GET'])
def get_cached_queries():
    v = cache.cache.get_many(*cached_keys)
    return json.dumps(v)


if __name__ == "__main__":
    api.run(debug=True)
