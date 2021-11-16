import os, configparser

from . import caching
from flask import Flask
from flask_caching import Cache


config = configparser.ConfigParser()
config.read('config.ini')

endpoint = config['OPENWEATERAPI']['endpoint']
key = config['OPENWEATERAPI']['key']
cache_ttl = int(os.environ.get('CACHE_TTL', 300))
default_max_number = int(os.environ.get('DEFAULT_MAX_NUMBER', 5))

def create_app():
    config = {
            "DEBUG": True,
            "CACHE_TYPE": "SimpleCache",
            "CACHE_DEFAULT_TIMEOUT": cache_ttl
            }

    cached_keys = []

    api = Flask(__name__)
    api.config.from_mapping(config)
    flask_cache = Cache(api)
    cache = caching.Cache(flask_cache)
    return api, cache

