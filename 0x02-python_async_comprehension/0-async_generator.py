#!/usr/bin/env python3
"""Simple Async_generator"""
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """
    An async generator waits 1 second and yields a random
    number 10 time between 0-10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
