#!/usr/bin/env python3
"""Callable return function"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float multiplier as an argument and returns a funtions multiplies a float by the given multiplier
    """
    def multiplier(value: float) -> float:
        return multiplier * value

    return multiplier
