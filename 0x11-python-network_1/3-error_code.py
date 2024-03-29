#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            html = resp.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
