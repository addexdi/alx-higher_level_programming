#!/usr/bin/python3

"""
    using request to get
    - content type
    - and OK status code from a URL
"""

import requests

if __name__ == "__main__":
    with requests.get("https://alx-intranet.hbtn.io/status") as res:
        print("Body response:")
        print("\t- type: {}".format(type(res.text)))
        print("\t- content: {}".format(res.text))
