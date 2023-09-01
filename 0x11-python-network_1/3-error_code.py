#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module takes in a URL, sends a request to the URL
and displays the body of the response.

Example:
    $ ./3-error_code.py http://0.0.0.0:5000

"""


if __name__ == '__main__':
    import urllib.request
    from urllib.error import HTTPError
    import sys
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
