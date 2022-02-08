"""Helpers methods."""
# TYPE CHECKING
from sanic.response import HTTPResponse

from sanic.response import json


def json_list_response(element: list) -> HTTPResponse:
    return json({
        'count': len(element),
        'values': element,
    })