#!/usr/bin/env python3
"""typing module for iterable and sequence"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """element length to get lenght of each sequence in the iterable"""
    return [(i, len(i)) for i in lst]
