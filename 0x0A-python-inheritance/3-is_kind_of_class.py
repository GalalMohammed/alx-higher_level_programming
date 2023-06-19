#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines is_kind_of_class function.

Example:
    a = 1
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))

"""


def is_kind_of_class(obj, a_class):
    """evaluates if object is an instance of a_class.

    Args:
        obj (object): obj to be checked.
        a_class (object): class to be compared to.

    Retunrs:
        True if obj is an instance of a_class, otherwise False.

    """
    return isinstance(obj, a_class)
