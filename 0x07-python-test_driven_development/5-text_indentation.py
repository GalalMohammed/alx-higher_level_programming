#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This is text indentation module.

This module supplies one function, text_indentation().
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters:
    ., ? and :
    
    Args:
        text: string.

    Raises:
        TypeError: if text isn't a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print("\n")
            i += 1
            while text[i] == ' ':
                i += 1
        else:
            i += 1
