#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for idx, j in enumerate(i):
            print("{:d}".format(j), end="")
            if not idx == len(i) - 1:
                print(" ", end="")
        print()