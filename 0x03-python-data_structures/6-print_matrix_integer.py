#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for idx, j in enumerate(matrix[i]):
            print("{:d}".format(j), end="")
            if not idx == len(matrix[i]) - 1:
                print(" ", end="")
        print()
    if matrix == [[]]:
        print()
