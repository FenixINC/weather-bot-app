from dataclasses import dataclass


@dataclass
class WeatherResponse:
    id: int
    name: str
    temperature: str
    description: str
