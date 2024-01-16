#!/usr/bin/env python3
"""Script for the coroutine measure_runtime"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    It will execute async_comprehension 4times in || using asyncio.gather
    measure_runtime should measure the total runtime and return it
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
