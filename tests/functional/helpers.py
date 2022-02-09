"""Helpers methods for tests."""
# TYPE CHECKING
from typing import Any

from enum import Enum


def deep_replace_enums(element: Any) -> Any:
    if isinstance(element, dict):
        return {k: deep_replace_enums(v) for k, v in element.items()}
    if isinstance(element, list):
        return [deep_replace_enums(_) for _ in element]
    if isinstance(element, Enum):
        return element.value
    return element
