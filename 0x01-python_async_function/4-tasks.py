#!/usr/bin/env python3
"""Script for the async funcition task_wait_n"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routine called task_wait_n, takes in 2 arguments: n and max_delay.
    It will spawn task_wait_random task n times with the specified max_delay.
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
