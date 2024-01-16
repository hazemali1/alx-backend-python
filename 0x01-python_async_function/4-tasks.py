#!/usr/bin/env python3
"""async functions"""
import asyncio
import typing


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """wait loof"""
    lis: typing.List[float] = []
    llis: typing.List[float] = []
    for _ in range(n):
        t: float = wait_random(max_delay)
        lis.append(t)
    for i in asyncio.as_completed(lis):
        llis.append(await i)
    return llis
