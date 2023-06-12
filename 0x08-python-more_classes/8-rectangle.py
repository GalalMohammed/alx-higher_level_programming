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

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """__init__ method.

        Args:
            width (int): rectangle width.
            height (int): rectangle height.

        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """Returns current rectangle area.

        Returns:
            rectangle area.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns current rectangle perimeter.

        Returns:
            rectangle perimeter.

        """
        if self.__height and self.__width:
            return 2 * (self.__width + self.__height)
        else:
            return 0

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.

        Returns:
            biggest rectangle.

        Raises:
            TypeError: if rect_1 o rect_2 aren't rectangles.

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_2 if rect_2.area() > rect_1.area() else rect_1

    def __str__(self):
        """Retunrs the rectangle with print_symbol.

        Retunrs:
            print_symbol rectangle.

        """
        if self.__height and self.__width:
            return (str(self.print_symbol) * self.__width + "\n")\
                   * (self.__height - 1)\
                   + str(self.print_symbol) * self.__width
        else:
            return ""

    def __repr__(self):
        """Returns a string representation of the rectangle.

        Returns:
            rectangle string representation.

        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints a bye message."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
