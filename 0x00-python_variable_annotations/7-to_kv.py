#!/usr/bin/env python3
"""Sting and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function
    Returns a tuple with string and float
    """
    return (k, float(v ** 2))
