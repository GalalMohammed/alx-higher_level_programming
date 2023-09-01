#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response.

Example:
    $ ./2-post_email.py

"""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
