#!/usr/bin/python3
"""
    use urllib
    - get the X-Request-Id
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        content = res.read()

    print(res.headers['X-Request-Id'])
