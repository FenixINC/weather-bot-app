from dataclasses import dataclass


@dataclass
class ErrorResponse:
    error_message: str
    error_code: int
