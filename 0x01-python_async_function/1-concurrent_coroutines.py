#!/usr/bin/env python3
"""Script for the async routine wait_n"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routine that takes in 2 int arguments: n and max_delay
    will spawn wait_random n times with the specified max_delay
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
