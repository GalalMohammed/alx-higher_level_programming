#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines square class.

Example:
    s = Square(13)

"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class defines square."""

    def __init__(self, size):
        """__init__ method.

        Args:
            size (int): square size.

        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """computes square area.

        Return:
            square area.

        """
        return self.__size ** 2
