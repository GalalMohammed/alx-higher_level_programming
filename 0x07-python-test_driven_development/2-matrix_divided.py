#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This is matrix divider module.

This module supplies one function, matrix_divided().

Example:
    >>> matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.

    Args:
        matrix: list of lists of numbers
        div: number.

    Returns:
        a new matrix.

    Raises:
        TypeError: if matris is not a list of lists of numbers, has different
            rows lengths, or div isn't a number.
        ZeroDivisionError: if div equals zero.

    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err_msg)
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(row, list):
            raise TypeError(err_msg)
        for i in row:
            if not type(i) in [int, float]:
                raise TypeError(err_msg)
    if not type(div) in [int, float]:
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]
