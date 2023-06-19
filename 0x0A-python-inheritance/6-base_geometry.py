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
