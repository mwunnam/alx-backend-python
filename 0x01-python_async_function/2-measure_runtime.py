#!/usr/bin/env python3
"""Function to measure the average time taken to run wait_n function"""
import time
from typing import List
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function to measure time used to run multiple coroutines

    Args:
        n (int): Number of coroutines to be run
        max_delay (int): Maximum delay for the coroutines

    Return:
        float: Average time per coroutine
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
