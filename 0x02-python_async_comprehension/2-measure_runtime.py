#!/usr/bin/env python3
"""Time Run time for async compressions"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This to measure the time taken to run 4 async_compression parallel
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    runtime = end_time - start_time
    return runtime
