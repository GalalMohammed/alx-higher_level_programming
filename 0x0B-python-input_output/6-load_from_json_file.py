#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines load_from_json_file function.

Example:
    filename = "my_list.json"
    my_list = load_from_json_file(filename)

"""

import json


def load_from_json_file(filename):
    """creates an Object from a JSON file.

    Args:
        filename (str): file name.

    Retunrs:
        object.

    """
    with open(filename) as file:
        return json.loads(file.read())
