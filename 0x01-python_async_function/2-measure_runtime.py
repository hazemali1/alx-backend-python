#!/usr/bin/env python3
"""async functions"""
wait_n = __import__('1-concurrent_coroutines').wait_n


import asyncio
import time


def measure_time(n, max_delay) -> float:
    """measure time"""
    start = time.time()
    lis = asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n