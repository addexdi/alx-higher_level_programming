#!/usr/bin/python3
"""
    use urllib to request a page
    traps an exception and print the error code
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as res:
            content = res.read()
            print(content.decode('UTF-8'))
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print('Error code:', e.code)
        else:
            pass
