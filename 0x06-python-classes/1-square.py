#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Class Square Docstring.

This module defines a class Square.

Example:
    You can define a square::

        my_square = Square(3)

"""


class Square:
    """A class defines a square.

    """

    def __init__(self, size):
        """__init__ method.

        Args:
            size (float): The size of square.

        """
        self.__size = size
