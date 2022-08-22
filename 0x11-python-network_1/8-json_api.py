#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    data = {}
    
    # defining data variables
    if len(argv) > 1:
        data['q'] = sys.argv[1]
    else:
        data['q'] = ''
    
    # request
    resp = requests.post(url, data=data)

    # interpreting json
    try:
        json_resp = resp.json()
        if json_resp == {}:
            print('No result')
        else:
            print("[{}] {}".format(json_resp.get("id"), json_resp.get("name")))
    except ValueError:
        print('Not a valid JSON')
