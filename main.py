


THUNDERSTORM = range(200, 300)
DRIZZLE = range(300, 400)
RAIN = range(500, 600)
SNOW = range(600, 700)
ATMOSPHERE = range(700, 800)
CLEAR = range(800, 801)
CLOUDY = range(801, 900)


# def display_weather_info(weather_response: WeatherResponse, imperial=False):
#     weather_id = weather_response.id
#     city = weather_response.name
#     weather_description = weather_response.description
#     temperature = weather_response.temperature
#
#     style.change_color(style.REVERSE)
#     print(f"{city:^{style.PADDING}}", end="")
#     style.change_color(style.RESET)
#
#     weather_symbol, color = _select_weather_display_params(weather_id)
#
#     style.change_color(color)
#
#     print(f"\t{weather_symbol}", end=" ")
#     print(f"{weather_description.capitalize():^{style.PADDING}}", end=" ", )
#     style.change_color(style.RESET)
#     print(f"({temperature}°{'F' if imperial else 'C'})")
#
#
# def show_error(error_response: ErrorResponse):
#     # TODO: show error
#     print(f"{error_response.error_message}")

# def _select_weather_display_params(weather_id):
#     # TODO: rewrite to 'match case'
#     if weather_id in THUNDERSTORM:
#         display_params = ("💥️", style.RED)
#     elif weather_id in DRIZZLE:
#         display_params = ("💧️", style.CYAN)
#     elif weather_id in RAIN:
#         display_params = ("💦️", style.BLUE)
#     elif weather_id in SNOW:
#         display_params = ("⛄️", style.WHITE)
#     elif weather_id in ATMOSPHERE:
#         display_params = ("🌀️", style.BLUE)
#     elif weather_id in CLEAR:
#         display_params = ("🔆️", style.YELLOW)
#     elif weather_id in CLOUDY:
#         display_params = ("💨️", style.WHITE)
#     else:  # In case the API adds new weather codes
#         display_params = ("🌈️", style.RESET)
#     return display_params

# def run:
# user_args = user_cli_args_config.read_user_cli_args()
# response_data = weather_controller.get_weather_data(city=user_args.city, imperial=user_args.imperial)
# if isinstance(response_data, WeatherResponse):
#     display_weather_info(weather_response=response_data, imperial=False)
# elif isinstance(response_data, ErrorResponse):
#     show_error(error_response=response_data)
