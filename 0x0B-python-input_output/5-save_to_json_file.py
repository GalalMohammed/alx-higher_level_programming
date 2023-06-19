#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines save_to_json_file function.

Example:
    filename = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename)

"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (object): object to be wrote.
        filename (str): file name.

    """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
