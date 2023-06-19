#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines MyList class.

Example:
    my_list = MyList()

"""


class MyList(list):
    """Class inherits from list."""

    def print_sorted(self):
        """prints the sorted list."""
        print(sorted(self))
