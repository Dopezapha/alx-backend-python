#!/usr/bin/env python3

"""
An async routine called wait_n that takes in 2 int arguments (in this order):
n and max_delay, and spawns wait_random n times with the specified max_delay.
"""

import asyncio
from wait_random import wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Asynchronously spawns wait_random n times with the specified max_delay.
    """
    task = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*task)
    return delays
