#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module takes your GitHub credentials (username and password)
to display your id.

Example:
    $ ./10-my_github.py papamuziko cisfun

"""


if __name__ == '__main__':
    import requests
    import sys
    url = 'https://api.github.com/users/' + sys.argv[1]
    headers = {
            'Accept': "application/vnd.github+json",
            'Authorization': f'Bearer {sys.argv[2]}',
            'X-GitHub-Api-Version': '2022-11-28'
            }
    r = requests.get(url, headers=headers)
    print(r.json().get('id'))
