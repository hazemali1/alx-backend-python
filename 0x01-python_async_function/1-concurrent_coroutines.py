#!/usr/bin/env python3
"""async functions"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    lis: list = []
    for i in range(n):
        t: float = await asyncio.gather(wait_random(max_delay))
        lis.append(t)
    return lis
