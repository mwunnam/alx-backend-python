#!/usr/bin/env python3
"""Basics of async"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Function to wait at a random time and return the delayed time
    params: max_delay - integer which has a default of 10
    return: the delayed float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
