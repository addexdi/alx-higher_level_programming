#!/usr/bin/python3
"""
    using request module
    - to send a post request to a mail address
    - print the response by the page
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    addr = sys.argv[2]
    payload = {"email": addr}

    with requests.post(url, data=payload) as res:
        print(res.text)
