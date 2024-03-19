#!/usr/bin/env python3
""" Module Doc """
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Documentation"""
    
    lis = [async_comprehension() for i in range(4)]
    start = time.perf_counter()
    res = await asyncio.gather(*lis)
    finish = time.perf_counter()
    return finish - start
