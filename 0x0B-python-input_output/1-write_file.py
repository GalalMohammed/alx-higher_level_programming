#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines write_file function.

Example:
    characters = write_file("my_first_file.txt", "This School is so cool!\n")

"""


def write_file(filename="", text=""):
    """writes a string to a txt file.

    Args:
        filename (str): file name.
        text (str): text to be wrote.

    Returns:
        number of characters written.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
