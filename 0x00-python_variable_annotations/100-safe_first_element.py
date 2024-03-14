#!/usr/bin/env python3
"""
Documentation for module
"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
	lst : Sequence
    """
    if lst:
        return lst[0]
    else:
        return None
