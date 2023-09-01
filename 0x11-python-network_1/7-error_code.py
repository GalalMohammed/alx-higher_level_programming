#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module takes in a URL, sends a request to the URL
and displays the body of the response.

Example:
    $ ./7-error_code.py http://0.0.0.0:5000

"""


if __name__ == '__main__':
    import requests
    import sys
    r = requests.get(sys.argv[1])
    if r.status_code == requests.codes.ok:
            print(r.text)
    else:
        print("Error code:", r.status_code)
