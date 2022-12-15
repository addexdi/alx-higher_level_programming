#!/usr/bin/python3
"""
    use the urllib
    request a content using urlopen
    inspect content for:
        type
        content
        utf8-content
"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res1:
        content = res1.read()
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode('utf8')))
