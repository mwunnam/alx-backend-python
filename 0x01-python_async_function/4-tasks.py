#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function to run multiple coroutines at the same time
    params: n , max_delay
    return: list of all the delays float in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    completed, _ = await asyncio.wait(tasks)

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
