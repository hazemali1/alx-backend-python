#!/usr/bin/env python3
"""async functions"""
import asyncio
import random


async def wait_random(max_delay=10) -> float:
    """wait random"""
    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n

if __name__ == "__main__":
    """main"""
    asyncio.run(main())
