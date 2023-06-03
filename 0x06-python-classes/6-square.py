#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Class Square Docstring.

This module defines a class Square.

Example:
    You can define a square::

        my_square = Square(5, (1, 1))
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
        my_square.my_print()

"""


class Square(object):
    """A class defines a square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method.

        Args:
            size (int): The size of square.
            position (:obj:`tuple` of :obj: `int`): square position.

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """:obj:`tuple` of :obj: `int`: printing position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           isinstance(value[0], int) or isinstance(value[1], int) or\
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns current square area.

        Returns:
            square area.

        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#'.
        """
        print("\n" * self.__position[1]
              + (" " * self.__position[0] + "#" * self.__size + "\n")
              * self.__size, end="" if self.__size else "\n")
