#!/usr/bin/python3
for i in range(26):
    if not i == 4 and not i == 17:
        print("{:c}".format(i + 97), end='')
