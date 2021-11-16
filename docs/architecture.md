# App Definition

Wrapper for the [Open Weather API current weather data service](https://openweathermap.org/current) that returns a city's temperature, with caching, also allowing for the temperature of the latest queried cities that are still validly cached to be retrived.

---

# Architecture

## Technologies and Frameworks

- Python 3.8+
- Flask
- Flask-Caching
- Python Venv
- pyTest
- PyDantic
- Requests

## Endpoints

No authentication should be required for using either endpoint.

PATH    |   METHOD  |   DESCRIPTION
---     |   ---     |   ---
/temperature/<city_name>    |   GET |   Get the current temperature for the specified **city_name**, either from cache or from the Open Weather API, if not already cached (and still valid).  [Data mappings](#data) are described below
/temperature?max=<max_number>   |   GET | Get the cached temperatures for up to the latest **max_number** queried cities (through the above endpoint) that are still valid. If **max_number** is not provided, **default_max_number** should be used instead.  Multiple temperatures from the same city should not be returned and no requests to Open Weather API should be made by this endpoint.

## Cache

- Cache has a configurable **cache\_ttl**, after which cached entries are no longer
valid to be returned by either endpoints;
-  **cache_ttl** and **default_max_number** are service configurations retrieved from
environment variables, if such data is available, or defaulting to 5 minutes and 5 entries
respectively otherwise;

## Data

### Getting the Data

The data comes from the [Open Weather API current weather data service](https://openweathermap.org/current) or from a previous cached data from the weather api.

### Output Data format

RETURNED FIELD   |   ORIGIN  |   DESCRIPTION
---         |   ---             |   ---
min         |    main.temp_min  |   Minimum temperature in degrees Celsius.
max         |    main.temp_max  |   Maximum temperature in degrees Celsius.
avg         |    main.temp      |   Average temperature in degrees Celsius.
feels_like  |    main.feels_like|   Feels like temperature in degrees Celsius.
city.name   |    name           |   Queried city's name.
city.country|    sys.country    |   Queried city's country code in the ISO 3166-1 alpha 3 format.

#### Sucessfull return example:

```json
{
    min: 5,
    max: 10,
    avg: 7.5,
    feels_like: 12,
    city: {
        name: "Gumbaldia",
        country: "Ooo"
    }
}
```
