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

    Returns:
        a new matrix.

    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not (isinstance(matrix, list) and isinstance(matrix[0], list) and
       type(matrix[0][0]) in [int, float]):
        raise TypeError(err_msg)
    for row in matrix[1:]:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not type(div) in [int, float]:
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]
