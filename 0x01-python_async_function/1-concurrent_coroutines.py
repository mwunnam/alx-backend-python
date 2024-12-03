#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    Function to run multiple coroutines at the same time
    params: n , max_delay
    return: list of all the delays float in ascending order
    """
    delays = []
    for i in range n:
        delay = await wait_random(max_delay)
        delays.append(delay)

    return sort(delay)
