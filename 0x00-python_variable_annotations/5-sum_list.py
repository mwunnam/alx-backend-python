#!/usr/bin/env python3
""" Complex types - list of float"""


from typing import List


def sum_list(input_list: list[float]) -> float:
    """
    This gives the sum of the elemet in the list
    """
    sum: float = 0.0
    for item in input_list:
        sum += item

    return sum
