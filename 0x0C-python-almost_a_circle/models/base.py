#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines Base class.

Example:
    b1 = Base()
    print(b1.id)

"""

import json


class Base(object):
    """Base class for the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method.

        Args:
            id (int): object custom id.

        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = type(self).__nb_objects

    def integer_validator(self, name, value):
        """validates value.

        Args:
            name (str): var name.
            value (object): value to be validated.

        Raises:
            TypeError: if value is not int.

        """
        if not type(value) in [int]:
            raise TypeError(f"{name} must be an integer")

    def size_validator(self, name, value):
        """validates size.

        Args:
            name (str): var name.
            value (object): value to be validated.

        Raises:
            ValueError: if value <= 0

        """
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def position_validator(self, name, value):
        """validates position cordinate.

        Args:
            name (str): var name.
            value (object): value to be validated.

        Raises:
            ValueError: if value < 0

        """
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @staticmethod
    def to_json_string(list_dictionaries):
        """gets JSON string representation.
        Args:
            list_dictionaries (list): list of dictionaries.
        Returns:
            JSON string representation.
        """
        if not list_dictionaries:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """gets the list of the JSON string representation.
        Args:
            json_string (str): string representing a list of dictionaries.
        Returns:
            list.
        """
        if not json_string:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): list of instances.
        """
        if not list_objs:
            list_objs = []
        with open(f"{cls.__name__}.json", 'w') as file:
            file.write(Base.to_json_string([
                obj.to_dictionary() for obj in list_objs]))

    @classmethod
    def load_from_file(cls):
        """gets list of instances.
        Returns:
            list.
        """
        try:
            with open(f"{cls.__name__}.json") as file:
                list_dict = json.loads(file.read())
        except Exception:
            list_dict = []
        return [cls.create(**dic) for dic in list_dict]

    @classmethod
    def create(cls, **dictionary):
        """gets an instance with all attributes already set.
        Args:
            dictionary: Arbitrary keyword arguments.
        Returns:
            object.
        """
        if cls.__name__ =  "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
