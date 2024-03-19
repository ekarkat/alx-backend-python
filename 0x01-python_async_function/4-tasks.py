#!/usr/bin/env python3
""" Modul doc """
import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function doc"""
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))

    results = await asyncio.gather(*tasks)
    return sorted(results)
