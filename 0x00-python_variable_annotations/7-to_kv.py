#!/usr/bin/env python3
"""
Write a type-annotated function sum_list
which takes a list input_list of floats as argument
and returns their sum as a float.

"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    k: str
    v: list
    return : tupple
    """
    return (k, v**2)
