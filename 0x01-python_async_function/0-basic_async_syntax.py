#!/usr/bin/env python3
"""Script for the asynchronous coroutine wait_random"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in an integer argument
    and waits for a random delay between 0 and max_delay and returns it
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
