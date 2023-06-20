#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines square class.
Example:
    s = Square(13)
"""

Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """class defines square."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """:obj:`int`: square size."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute.
        Args:
            args: Variable length argument list.
            Kwargs: Arbitrary keyword arguments.
        """
        if len(args):
            setattr(self, "id", args[0])
            if len(args) > 1:
                setattr(self, "size", args[1])
            if len(args) > 2:
                setattr(self, "x", args[2])
            if len(args) > 3:
                setattr(self, "y", args[3])
        else:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """gets the dictionary representation.
        Returns:
            dict.
        """
        return {'id': self.id, 'size': self.width, 'x': self.x,
                'y': self.y}

    def __str__(self):
        """Returns a string representation of the square.
        Returns:
            square string representation.
        """
        return f"[Square] (self.id) {self.__x}/{self.__y}"\
                + f"- {self.__width}"
