import pytest, json

from api import endpoints


@pytest.fixture
def api():
    return endpoints.api.test_client()

def test_status_code(api):
    response = api.get('/temperature')

    assert 200 == response.status_code

def test_cache(api):
    response = api.get('/temperature/dota')
    assert 200 == response.status_code
    response = api.get('/temperature/curitiba')
    assert 200 == response.status_code
    response = api.get('/temperature/salvador')
    assert 200 == response.status_code
    response = api.get('/temperature/compton')
    assert 200 == response.status_code
    response = api.get('/temperature/lagos')
    assert 200 == response.status_code
    response = api.get('/temperature/taipei')
    assert 200 == response.status_code

    response = api.get('/temperature')
    js = json.loads(response.get_data())
    assert len(js) == 5

    citys = ['dota', 'curitiba', 'salvador', 'compton', 'lagos', 'taipei']
    for city_name, city in zip(reversed(citys), js):
        assert city_name == list(city.keys())[0]


def test_max_cache(api):
    response = api.get('/temperature/dota')
    assert 200 == response.status_code
    response = api.get('/temperature/curitiba')
    assert 200 == response.status_code
    response = api.get('/temperature/salvador')
    assert 200 == response.status_code
    response = api.get('/temperature/compton')
    assert 200 == response.status_code
    response = api.get('/temperature/lagos')
    assert 200 == response.status_code
    response = api.get('/temperature/taipei')
    assert 200 == response.status_code

    response = api.get('/temperature?max=6')
    js = json.loads(response.get_data())
    assert len(js) == 6

    citys = ['dota', 'curitiba', 'salvador', 'compton', 'lagos', 'taipei']
    for city_name, city in zip(reversed(citys), js):
        assert city_name == list(city.keys())[0]
