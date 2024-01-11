#!/usr/bin/env python3
"""Script for function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function make_multiplier
    takes a float as argument, returns a function that multiplies another by it
    """

    def multiply(another: float) -> float:
        """
        Type-annotated function takes a float and multiply it by multiplier
        """
        return another * multiplier

    return multiply
