#!/usr/bin/python3

"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    _payload = {"q": q}

    resp = requests.post(url, data=_payload)

    try:
        data = resp.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))

        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
