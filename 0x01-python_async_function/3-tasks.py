#!/urs/bin/env python3
"""Regular function that returns asyncio.Task object"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular functin that return an asyncio.Task.

    Args:
        max_delay (int): Maximum delay for wait_random coroutine

    Returns:
        asyncio.Task: A task object created for the waiting_random

    """
    return asyncio.create_task(wait_random(max_delay))
