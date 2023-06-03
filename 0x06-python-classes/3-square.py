#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Class Square Docstring.

This module defines a class Square.

Example:
    You can define a square::

        my_square = Square(5)
        print("Area: {}".format(my_square.area()))

"""


class Square:
    """A class defines a square.

    """

    def __init__(self, size=0):
        """__init__ method.

        Args:
            size (int): The size of square.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns current square area.

        Returns:
            square area.

        """
        return self.__size ** 2