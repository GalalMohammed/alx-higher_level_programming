#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines a function that returns list of available attributes and
methods of an object.

Example:
    print(lookup(int))
"""


def lookup(obj):
    """gets the list of available attributes and methods of an object.

    Args:
        obj (object): object to be used.

    Returns:
        a list.

    """
    return dir(obj)
