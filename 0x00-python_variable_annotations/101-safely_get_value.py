#!/usr/bin/env python3
"""Script for function safely_get_value"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Type-annotated function safely_get_value,
    takes a dictionary and a key as arguments, returns value or None
    """
    if key in dct:
        return dct[key]
    else:
        return default
