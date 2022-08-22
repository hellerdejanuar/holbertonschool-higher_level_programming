#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    import sys

    auth = (sys.argv[1], sys.argv[2])
    resp = requests.get('https://api.github.com/user', auth=auth)
    if resp.status_code < 400:
        print(resp.json().get('id'))
    else:
        print('None')
