#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.

Example:
    $ ./1-hbtn_header.py https://alx-intranet.hbtn.io

"""


if __name__ == '__main__':
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
