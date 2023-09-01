#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.

Example:
    $ ./8-json_api.py a

"""


if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) > 1:
        payload = {'q': sys.argv[1]}
    else:
        payload = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    if r.json():
        print(f"[{r.json()['id']}] {r.json()['name']}")
    else:
        print("No result")
