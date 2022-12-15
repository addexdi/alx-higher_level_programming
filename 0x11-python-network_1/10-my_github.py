#!/usr/bin/python3
"""
    use request lib + git API
    - using basic authentication to get the user id
"""

import requests

import sys

if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth

    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)

    with requests.get("https://api.github.com/user", auth=auth) as res:
        response = res.json().get("id")
        print(response)
