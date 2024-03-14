#!/usr/bin/env python3
"""
Write a type-annotated function sum_list
which takes a list input_list of floats as argument
and returns their sum as a float.

"""
from typing import List


def sum_list(input_list: list[float]) -> float:
    """
    input_list : float
    return : float
    """
    sum_input = 0
    for n in input_list:
        sum_input = sum_input + n
    return sum_input
