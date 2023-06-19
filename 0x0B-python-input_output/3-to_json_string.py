#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines to_json_string function.

Example:
    my_list = [1, 2, 3]
    s_my_list = to_json_string(my_list)

"""

import json


def to_json_string(my_obj):
    """converts an object to JSON representation.

    Args:
        my_obj (object): object to be converted.

    Returns:
        JSON representation.

    """
    return json.dumps(my_obj)
