try:
    from app import schemas, open_weather_api, create_app, default_max_number, endpoint, key
except:
    from api.app import schemas, open_weather_api, create_app, default_max_number, endpoint, key

from flask import json, request


api, mycache = create_app()

@api.route('/temperature/<city>', methods=['GET'])
def get_weather(city: str):
    weather = mycache.get(city)
    if weather is None:
        data = open_weather_api.get_data(city, endpoint=endpoint, key=key)
        weather = open_weather_api.transform_data(data)
        if weather == "error":
            return json.dumps({"message": "City not found."}), 401
        mycache.set(city, weather)
        return json.dumps(weather)
    return json.dumps(weather)

@api.route('/temperature', methods=['GET'])
def get_cached_weather():
    # query parameter
    max_number = int(request.args.get('max', default_max_number))
    
    keys = mycache.keys
    r = [{k: mycache.get(k)} for k in keys]
    rsult = [re for re in reversed(r)]

    if len(rsult) > max_number:
        return json.dumps(rsult[:max_number])
    return json.dumps(rsult)


if __name__ == "__main__":
    api.run(debug=True)

