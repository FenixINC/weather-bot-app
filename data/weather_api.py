from urllib import parse

from configs import api_config
from constants import BASE_WEATHER_API_URL


def get_weather_url_by_city_name(city_input, imperial=False):
    """Builds the URL for an API request to OpenWeather's weather API.

    Args:
        city_input (List[str]): Name of a city as collected by argparse
        imperial (bool): Whether or not to use imperial units for temperature

    Returns:
        str: URL formatted for a call to OpenWeather's city name endpoint

    """

    api_key = api_config.get_api_key()
    city_name = "".join(city_input)
    url_encoded_city_name = parse.quote_plus(city_name)
    units = "imperial" if imperial else "metric"
    url = f"{BASE_WEATHER_API_URL}?q={url_encoded_city_name}"f"&units={units}&appid={api_key}"
    return url
