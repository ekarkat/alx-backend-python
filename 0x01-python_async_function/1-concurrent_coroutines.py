#!/usr/bin/env python3
""" Modul doc """
import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function doc"""
    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    results = await asyncio.gather(*tasks)
    return sorted(results)
