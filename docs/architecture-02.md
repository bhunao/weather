### 2

###### [previous](./architecture-01.md)

This file was made during the prototype process. Is to show my process of thoughts through the evolution of this file.

######  [next](./architecture-03.md)

---

# Questions for development

- What this app does?
- How Efficient it needs to be?
- How Scalabe it needs to be?
- How much testable it needs to be?
- How much coupling this project will have?
- What are the harder parts to develop?
- What are the easiest parts to develop?
- What you need to learn to fully developy this?
- Something in this project will need change in the future?
- Will this project be deployed?
- Type of architecture pattern on this project?
- Any of this questions are unnecessary?
- bruh, front-end?
- Need to storage data in any way?
- Is this Over engineered?
- MCV?
    - what is the model?
    - what is the controller?
    - what is the view?
- ?

# App Definition

Wrapper for the [Open Weather API current weather data service](https://openweathermap.org/current) that returns a city's temperature, with caching, also allowing for the temperature of the latest queried cities that are still validly cached to be retrived.

---

# Architecture

## Technologies and Frameworks

- Python 3.?
- Flask
    - -some-flask-plugins
- ?Docker
- pyTest or unitTest
- Schematics or pyDantic
- ?flask-caching

## Endpoints


No authentication should be required for using either endpoint.

PATH    |   METHOD  |   DESCRIPTION
---     |   ---     |   ---
/temperature/<city_name>    |   GET |   Get the current temperature for the specified **city_name**, either from cache or from the Open Weather API, if not already cached (and still valid).  [Data mappings](#data) are described below
/temperature?max=<max_number>   |   GET | Get the cached temperatures for up to the latest **max_number** queried cities (through the above endpoint) that are still valid. If **max_number** is not provided, **default_max_number** should be used instead.  Multiple temperatures from the same city should not be returned and no requests to Open Weather API should be made by this endpoint.

---

## Cache


- Cache should have a configurable **cache_ttl**, after which cached entries are no longer
valid to be returned by either endpoints;
-  **cache_ttl** and **default_max_number** should be service configurations retrieved from
environment variables, if such data is available, or defaulting to 5 minutes and 5 entries
respectively otherwise;
- Created interface-alike object to get all the key values.

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

## Testing

TDD ...

## Planning

1. Plan Architecture
2. Prototype  
    2.1 API Server Mock
3. First batch of Tests and development
4. Open Api tests
5. front-end
6. Docker?
7. tests and more tests, and maybe a

99. README.md with full instructions on how to run both the services as well as it's automated tests.
