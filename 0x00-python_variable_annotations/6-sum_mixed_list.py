#!/usr/bin/env python3
from typing import List, Union
"""Complex types -mixed list"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Adds all items in the list
    """
    return float(sum(mxd_lst))
