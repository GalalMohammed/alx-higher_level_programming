#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines class_to_json function.

Example:
    m = MyClass("John")
    mj = class_to_json(m)

"""

json = __import__('json')


def class_to_json(obj):
    """creates dictionary for JSON serialization of an object.

    Args:
        obj (object): class to be converted.

    Returns:
        dictionary.

    """
    return json.dumps(obj.__dict__)
