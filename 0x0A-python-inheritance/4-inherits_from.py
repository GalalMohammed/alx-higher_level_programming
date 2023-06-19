#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines inherits_from function.

Example:
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))

"""


def inherits_from(obj, a_class):
    """evaluates if obj is an instance of a class that inherited from a_class.

    Args:
        obj (object): obj to be checked.
        a_class (object): class to be compared to.

    Returns:
        True if obj is an instance of a sub class of a_class, otherwise False.

    """
    return isinstance(obj, a_class) and not type(obj) in [a_class]
