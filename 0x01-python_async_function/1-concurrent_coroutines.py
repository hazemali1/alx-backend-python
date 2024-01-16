#!/usr/bin/env python3
"""async functions"""
import asyncio
import typing


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """wait loof"""
    lis: typing.List[float] = []
    for _ in range(n):
        t: float = await wait_random(max_delay)
        lis.append(t)
    return lis
