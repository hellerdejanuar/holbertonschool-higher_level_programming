#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests

    resp = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(resp.text)))
    print('\t- content: {}'.format(resp.text))
