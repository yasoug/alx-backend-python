#!/usr/bin/env python3
"""Script for function sum_mixed_list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Type-annotated function sum_mixed_list,
    takes a list of of integers and floats and returns their sum as a float
    """
    return sum(mxd_lst)
