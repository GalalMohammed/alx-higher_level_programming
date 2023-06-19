#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines from_json_string function.

Example:
    s_my_list = "[1, 2, 3]"
    my_list = from_json_string(s_my_list)

"""

import json


def from_json_string(my_obj):
    """converts a JSON representation to python data structure.

    Args:
        my_obj (object): object to be converted.

    Returns:
        object.

    """
    return json.loads(my_obj)
