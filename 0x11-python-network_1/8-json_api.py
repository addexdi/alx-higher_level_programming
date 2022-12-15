#!/usr/bin/python3
"""
    send a mail request using post
    - return the id and name
"""
import requests
import sys

if __name__ == "__main__":
    content = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {'q': content}

    with requests.post("http://0.0.0.0:5000/search_user", data=payload) as r:
        try:
            response = r.json()
            if response == {}:
                print("No result")
            else:
                print\
                    ("[{}] {}".format(response.get('id'), response.get('name')))
        except ValueError:
            print("Not a valid JSON")
