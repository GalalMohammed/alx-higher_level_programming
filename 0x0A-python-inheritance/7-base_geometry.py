#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines BaseGeometry class.

Example:
    bg = BaseGeometry()

"""


class BaseGeometry(object):
    """class defines a BaseGeometry."""

    def area(self):
        """raises an Exception.

        Raises:
            Exception.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value.

        Args:
            name (str): var name.
            value (object): value to be validated.

        Raises:
            TypeError: if value is not int.
            ValueError: if value <= 0.

        """
        if not type(name) in [int]:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
