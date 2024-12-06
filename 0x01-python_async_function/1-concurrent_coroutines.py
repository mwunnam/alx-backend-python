#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function to run multiple coroutines at the same time
    params: n , max_delay
    return: list of all the delays float in ascending order
    """
    delays = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        delays.append(task)

    completed, _ = await asyncio.wait(delays)

    results = [task.result() for task in completed]

    sorted_results = []
    for delay in results:
        for i, val in enumerate(sorted_results):
            if delay < val:
                sorted_results.insert(i, delay)
                break
        else:
            sorted_results.append(delay)

    return sorted_results
