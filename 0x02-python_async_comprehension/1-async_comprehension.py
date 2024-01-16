#!/usr/bin/env python3
"""async function"""
import asyncio
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """async comprehension function"""
    result: typing.List = []
    async for i in async_generator():
        result.append(i)
    return result
