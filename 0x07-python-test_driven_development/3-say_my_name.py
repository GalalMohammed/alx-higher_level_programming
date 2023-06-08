#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This is Say My Name module.

This module supplies one function, say_my_name().

Example:
    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob
"""


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
