#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Class Square Docstring.

This module defines a class Square.

Example:
    You can define a square::

        my_square = Square(5)
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))

"""


class Square:
    """A class defines a square.

    """

    def __init__(self, size=0):
        """__init__ method.

        Args:
            size (int): The size of square.

        """
        self.size = size

    @property
    def size(self):
        """:obj:`int`: size of square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current square area.

        Returns:
            square area.

        """
        return self.__size ** 2
