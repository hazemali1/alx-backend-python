#!/usr/bin/env python3
"""typing module for Union here"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """sum_mixed_list function for sum list"""
    return sum(mxd_lst)
