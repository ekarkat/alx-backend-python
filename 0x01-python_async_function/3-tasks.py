#!/usr/bin/env python3
import asyncio
import time

async def new():
    print('A')
    time.sleep(2) 
    print('B')

async def num():
    print('1')
    time.sleep(2) 
    print('2') 


def num2():
    print('3')
    print('4')

asyncio.run(new())

num2()