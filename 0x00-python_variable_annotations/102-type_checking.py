#!/usr/bin/env python3
"""module typing"""
import typing


def zoom_array(lst: typing.Tuple[any, ...], factor: int = 2) -> typing.List:
    """zoom for array"""
    zoomed_in: typing.Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
