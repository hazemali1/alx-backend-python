#!/usr/bin/env python3
"""typing module for callable"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """make a multiplier return function that multiplies"""
    def fun(v: float) -> float:
        return multiplier * v
    return fun
