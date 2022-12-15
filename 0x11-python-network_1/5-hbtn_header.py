#!/usr/bin/python3

"""
    using request to get
    - content type
    - and OK status code from a URL
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with requests.get(url) as res:
        print(res.headers.get("X-Request-Id"))
