import json
from urllib import error
from urllib import request

from data import weather_api
from data.response.ErrorResponse import ErrorResponse
from data.response.WeatherResponse import WeatherResponse


def get_weather_data(city, imperial):
    try:
        response = request.urlopen(
            weather_api.get_weather_url_by_city_name(
                city_input=city,
                imperial=imperial
            )
        )
    except error.HTTPError as http_error:
        match http_error:
            case 400:
                error_response = ErrorResponse(
                    error_message="Bad request",
                    error_code=http_error.code
                )
                return error_response
            case 401:
                error_response = ErrorResponse(
                    error_message="Unauthorized",
                    error_code=http_error.code
                )
                return error_response
            case 403:
                error_response = ErrorResponse(
                    error_message="Forbidden",
                    error_code=http_error.code
                )
                return error_response
            case 404:
                error_response = ErrorResponse(
                    error_message="Not found",
                    error_code=http_error.code
                )
                return error_response
            case _:
                error_response = ErrorResponse(
                    error_message="Something went wrong...",
                    error_code=http_error.code
                )
                return error_response

    weather_data = json.loads(response.read())

    try:
        weather_response = WeatherResponse(
            id=weather_data["weather"][0]["id"],
            name=weather_data["name"],
            description=weather_data["weather"][0]["description"],
            temperature=weather_data["main"]["temp"]
        )

        return weather_response
    except json.JSONDecodeError:
        error_response = ErrorResponse(
            error_message="Couldn't read the server response.",
            error_code=400
        )
        return error_response
