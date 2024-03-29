#!/usr/bin/python3
"""
this python script takes in a URL, sends a request (using requests)
to the URL and displays the value of the X-Request-Id variable found
in the header of the response.
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    data = {'email': argv[2]}
    resp = requests.post(argv[1], data)
    print(resp.text)
