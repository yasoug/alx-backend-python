#!/usr/bin/env python3
"""Script for the coroutine async_comprehension"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that takes no arguments, it will collect 10 random numbers
    using an async comprehensing over async_generator and return the 10 numbers
    """
    return [num async for num in async_generator()]
