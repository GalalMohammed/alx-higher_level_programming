#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines s simple rectangle class.

Example:
    You can define a rectangle::
        my_rectangle = Rectangle()
        my_rectangle.width = 10
        my_rectangle.height = 3

"""


class Rectangle(object):
    """Class defines a rectangle."""

    def __init__(self, width=0, height=0):
        """__init__ method.

        Args:
            width (int): rectangle width.
            height (int): rectangle height.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """:obj:`int`: rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """:obj:`int`: rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
