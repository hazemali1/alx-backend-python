#!/usr/bin/env python3
"""modules types for Nonetype module typing"""
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]
                       ) -> typing.Union[typing.Any, None]:
    """safe first element"""
    if lst:
        return lst[0]
    else:
        return None
