#!/usr/bin/python3

""" 
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,

"""

import requests
import sys

if __name__ == "__main__":

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    resp = requests.get(url)

    if resp.status_code == 200:
        coms = resp.json()[:10]

        for c in coms:
            sha = c['sha']
            author_name = c['commit']['author']['name']
            print(f"{sha}: {author_name}")

    else:
        print("Error: Failed to retrieve commits from the repository")
