#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines Student class.

Example:
    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

"""


class Student(object):
    """class defines a student."""

    def __init__(self, first_name, last_name, age):
        """__init__ method.

        Args:
            first_name (string): first name.
            last_name (string): last name.
            age (int): student age.

        """
        self.first_name = first_name
        self.last_nama = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance.

        Retunrs:
            a dict.

        """
        return self.__dict__
