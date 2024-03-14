#!/usr/bin/env python3
"""
Write a type-annotated function sum_list
which takes a list input_list of floats as argument
and returns their sum as a float.

"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    lis : Sequence
    Callable : list float
    return : Float
    """
    return [(i, len(i)) for i in lst]
