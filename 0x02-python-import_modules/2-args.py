#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    print("{:d} argument".format(argc), end="")
    if argc:
        if not argc == 1:
            print("s", end="")
        print(":")
        for c, v in enumerate(sys.argv[1:]):
            print("{:d}: {:s}".format(c + 1, v))
    else:
        print("s.")
