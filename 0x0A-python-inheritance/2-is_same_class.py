#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines is_same_class function.

Example:
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))

"""


def is_same_class(obj, a_class):
    """evaluates if obj is an instance of a_class.

    Args:
        onj (object): obj to be checked.
        a_class (object): class to be compared to.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False

    """
    return type(obj) in [a_class]
