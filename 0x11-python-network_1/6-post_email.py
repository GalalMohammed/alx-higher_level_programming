#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response.

Example:
    $ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com

"""


if __name__ == '__main__':
    import requests
    import sys
    payload = {'email': sys.argv[2]}
    r = requests.get(sys.argv[1], params=payload)
    print(r.text)
