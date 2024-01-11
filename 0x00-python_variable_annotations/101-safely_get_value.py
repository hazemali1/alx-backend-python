#!/usr/bin/env python3
"""module typing"""
import typing


T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any,
                     default: typing.Union[T, None]
                     ) -> typing.Union[typing.Any, T]:
    """safely get value"""
    if key in dct:
        return dct[key]
    else:
        return default
