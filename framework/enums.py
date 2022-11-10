from enum import Enum


class HTTPMethod(str, Enum):
    GET = "GET"
    POST = "POST"
