#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response
"""

from sys import argv
from urllib import request, parse
import urllib.error

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as resp:
            html = resp.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as error:
        print(f'Error code: {error.code}')
        raise
