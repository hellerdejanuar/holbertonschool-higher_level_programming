#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL0 (with requests)
and displays the body of the response
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    resp = requests.get(argv[1])

    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
