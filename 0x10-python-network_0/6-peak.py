#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines find_peak function.

Example:
    print(find_peak([1, 2, 4, 6, 3]))

"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers.
    Args:
        list_of_integers (list): integers to be used.
    Returns:
        peak element.
    """
    len_of_list = len(list_of_integers)
    for i, e in enumerate(list_of_integers):
        if i < len_of_list - 1 and e <= list_of_integers[i + 1]:
            continue
        elif 0 < i < len_of_list - 1 and e <= list_of_integers[i - 1]:
            continue
        else:
            return e
