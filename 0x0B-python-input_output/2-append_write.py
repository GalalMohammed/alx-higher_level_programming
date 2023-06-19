#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines append_write function.

Example:
    characters = append_write("file_append.txt", "This School is so cool!\n")

"""


def append_write(filename="", text=""):
    """appends a string at the end of a txt file.

    Args:
        filename (str): file name.
        text (str): text to be appended.

    Returns:
        number of characters added.

    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
