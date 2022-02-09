"""Helpers methods."""
# TYPE CHECKING
from sanic.response import HTTPResponse
from typing import Any

from sanic.response import json
from copy import deepcopy
from enum import Enum


def _deep_replace_enums(element: Any) -> Any:
    if isinstance(element, dict):
        return {k: _deep_replace_enums(v) for k, v in element.items()}
    if isinstance(element, list):
        return [_deep_replace_enums(_) for _ in element]
    if isinstance(element, Enum):
        return element.value
    return element


def json_list_response(elements: list) -> HTTPResponse:
    return json({
        'count': len(elements),
        'values': _deep_replace_enums(deepcopy(elements)),
    })