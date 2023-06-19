#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines read_file function.

Example:
    read_file("my_file_0.txt")

"""


def read_file(filename=""):
    """reads a txt file and prints it.

    Args:
        filename (str): file name.

    """
    with open(filename, encoding='utf-8') as file:
        print(file.read())
