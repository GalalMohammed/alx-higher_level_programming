#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines Rectangle class.

Example:
    r1 = Rectangle(10, 2)

"""

from base import Base


class Rectangle(Base):
    """class defines a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method.

        Args:
            width (int): rectange width.
            height (int): rectangle height.
            x (int): horizontal coordinate.
            y (int): vertical coordinate.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """:obj:`int`: rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.size_validator("width", value)
        self.__width = value
    
    @property
    def height(self):
        """:obj:`int`: rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.size_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """:obj:`int`: rectangle x position."""
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.position_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """:obj:`int`: rectangle y position."""
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.position_validator("y", value)
        self.__y = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute.
        Args:
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        if len(args):
            setattr(self, "id", args[0])
            if len(args) > 1:
                setattr(self, "width", args[1])
            if len(args) > 2:
                setattr(self, "height", args[2])
            if len(args) > 3:
                setattr(self, "x", args[3])
            if len(args) > 4:
                setattr(self, "y", args[4])
        else:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])

    def area(self):
        """computes rectangle area.

        Returns:
            rectangle area.

        """
        return self.__width * self.__height

    def display(self):
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

    def to_dictionary(self):
        """gets the dictionary representation.
        Returns:
            dict.
        """
        return {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y}

    def __str__(self):
        """Returns a string representation of the rectangle.
        Returns:
            rectangle string representation.
        """
        return f"[Rectangle] (self.id) {self.__x}/{self.__y}"\
               + f"- {self.__width}/{self.__height}"
