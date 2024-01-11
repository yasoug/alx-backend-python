#!/usr/bin/env python3
"""Script for function safe_first_element"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Type-annotated function safe_first_element,
    takes a sequence of any type as argument and returns any or None
    """
    if lst:
        return lst[0]
    else:
        return None
