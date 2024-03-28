#!/usr/bin/python3

"""
This script takes a URL as input, sends a request to the URL,
and displays the value of the variable X-Request-Id in
the response header
"""

import sys
import requests


if __name__ == "__main__":

    url = sys.argv[1]
    resp = requests.get(url)
    request_id = resp.headers.get('X-Request-Id')

    print(request_id)
