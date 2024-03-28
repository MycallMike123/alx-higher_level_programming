#!/usr/bin/python3

"""Script that fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(url)
    cont = resp.text
    print("Body response:")
    print("\t- type:", type(cont))
    print("\t- content:", cont)
