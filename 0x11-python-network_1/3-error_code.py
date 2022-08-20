#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response
"""

if __name__ == "__main__":
    from sys import argv
    import urllib.request

    with request.urlopen(argv[1]) as resp:
        try:
            html = resp.read()
            print(html.decode('utf-8'))
        except urllib.error.HTTPError as error:
            print('Error code: {}'.format(error.code))
