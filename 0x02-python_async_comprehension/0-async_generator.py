#!/usr/bin/env python3
""" Module Doc """
import asyncio
import random
from typing import Generator


async def async_comprehension() -> Generator[float, None, None]:
    """Documentation"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
