#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines Rectangle class.

Example:
    r = Rectangle(3, 5)

"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class defines a rectangle."""

    def __init__(self, width, height):
        """__init__ method.

        Args:
            width (int): rectangle width.
            height (int): rectangle height.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area():
        """computes rectangle area.

        Retunrs:
            rectangle area.

        """
        return self.__width * self.__height

    def __str__(self):
        """description.

        Returns:
            rectangle description.

        """
        return f"[Rectangle] {self.__width}/{self.__height}"
