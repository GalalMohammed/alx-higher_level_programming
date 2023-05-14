#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    match sys.argv[2]:
        case "+":
            print("{:d} + {:d} = {}".format(a, b, add(a, b)))
        case "-":
            print("{:d} - {:d} = {}".format(a, b, sub(a, b)))
        case "*":
            print("{:d} * {:d} = {}".format(a, b, mul(a, b)))
        case "/":
            print("{:d} / {:d} = {}".format(a, b, div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
