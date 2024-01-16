#!/usr/bin/env python3
"""async function"""
import asyncio
import random


async def numbers(numbers):
    """range of numbers"""
    for i in range(numbers):
        yield i


async def async_generator():
    """loop"""
    async for _ in numbers(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
