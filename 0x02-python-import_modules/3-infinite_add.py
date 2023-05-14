#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argsum = 0
    for v in sys.argv[1:]:
        argsum += int(v)
    print(argsum)
