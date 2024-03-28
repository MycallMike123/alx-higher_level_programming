#!/usr/bin/python3
"""
This script takes a URL and an email as input, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    _request = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(_request) as response:
        print(response.read().decode('utf-8'))
