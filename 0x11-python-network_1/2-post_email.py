#!/usr/bin/python3
"""
this python script takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""

from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    data = parse.urlencode({'email': argv[2], 'method': 'POST'})
    data = data.encode('ascii')

    req = request.Request(argv[1], data)

    with request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
        print(html)
