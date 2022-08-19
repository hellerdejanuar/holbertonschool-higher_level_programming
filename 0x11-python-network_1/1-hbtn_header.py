#!/usr/bin/python3
"""this python script fetches https://intranet.hbtn.io/status"""

import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html_info = response.info()
        print(html_info.get('X-Request-Id'))
