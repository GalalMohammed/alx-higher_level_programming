#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This is the integers addition module.

This module supplies one function, add_integer().
Example:
    >>> add_integer(1, 2)
    3
"""


def add_integer(a, b=98):
    """adds 2 ints.

    Args:
        a: The first number.
        b(optional): The second number. Defaults to 98.

    Retunrs:
        The addition of int of a and int of b.

    Raises:
        TypeError: if a or b not numbers.

    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer("School")
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    """
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    if not type(b) in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
