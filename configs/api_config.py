from configparser import ConfigParser

from constants import SECRETS_INI_FILE


def get_api_key():
    """Fetch the API key from your configuration file.
    Expects a configuration file named "secrets.ini" with structure:
        [openweather]
        api_key=<YOUR-OPENWEATHER-API-KEY>
    """

    config = ConfigParser()
    config.read(SECRETS_INI_FILE)
    return config["openweather"]["api_key"]

def get_telegram_token():
    config = ConfigParser()
    config.read(SECRETS_INI_FILE)
    return config["openweather"]["telegram_token"]
