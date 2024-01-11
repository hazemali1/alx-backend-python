#!/usr/bin/env python3
"""typing module for tuple"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns a tuple"""
    return (k, v*v)
