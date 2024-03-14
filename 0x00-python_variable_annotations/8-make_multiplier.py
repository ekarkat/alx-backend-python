#!/usr/bin/env python3
"""
Write a type-annotated function sum_list
which takes a list input_list of floats as argument
and returns their sum as a float.

"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    multiplier : float
    Callable : list float
    return : Float
    """

    def foo(num: float):
        return num * multiplier

    return foo
