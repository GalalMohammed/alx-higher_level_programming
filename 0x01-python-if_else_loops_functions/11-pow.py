#!/usr/bin/python3
def pow(a, b):
    power = a
    if b > 0:
        for i in range(b - 1):
            power *= a
        return (power)
    elif b == 0:
        return (1)
    else:
        for i in range(-b - 1):
            power *= a
        return (1 / power)
