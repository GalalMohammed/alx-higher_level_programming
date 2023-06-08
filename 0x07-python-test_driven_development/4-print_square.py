#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This is square printer module.

This module supplies one function, print_square().

Example:
    >>> print_square(4)
    ####
    ####
    ####
    ####
"""


def print_square(size):
    """prints a square with the character #.

    Args:
        size: square length.

    Raises:
        TypeError: if size isn't an int.
        ValueError: if size < 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n")
          * size, end="" if size else "\n")
