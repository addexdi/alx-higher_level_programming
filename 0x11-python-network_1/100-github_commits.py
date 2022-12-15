#!/usr/bin/python3
'''
    Using requests lib to
    -get the last 6 commits of a user
    - uses git api https://api.github.com/repos/owner/repo/commits
'''
import requests
import sys

if __name__ == "__main__":
    owner = sys.argv[2]
    repo = sys.argv[1]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    with requests.get(url) as res:
        commits = res.json()
        try:
            for i in range(10):
                print("{}: {}".format(
                    commits[i].get("sha"),
                    commits[i].get("commit").get("author").get("name")))
        except IndexError:
            pass
