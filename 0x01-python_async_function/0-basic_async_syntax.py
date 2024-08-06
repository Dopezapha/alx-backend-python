#!/usr/bin/env python3

import asyncio
import random

"""
This module provides an asynchronous coroutine that waits for a random delay
between 0 and a given maximum delay (inclusive) and then returns the actual
delay waited.
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and max_delay seconds.
    """
    # Generate a random float between 0 and max_delay (inclusive)
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
