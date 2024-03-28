#!/usr/bin/python3

"""
This script takes a URL as input, sends a request to the URL,
and displays the valueof the X-Request-Id variable found in
the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        hr = response.info()
        print(hr['X-Request-Id'])
