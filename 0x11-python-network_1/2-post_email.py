#!/usr/bin/python3
"""
    use urllib to send post request
    attaches the mail to the url address
    displays the content
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    mail = sys.argv[2]
    url = sys.argv[1]

    value = {'email': mail}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    res = urllib.request.Request(url, data)

    with urllib.request.urlopen(res) as e_content:
        content = e_content.read()
        print(content.decode('utf-8'))
