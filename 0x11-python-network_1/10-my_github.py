#!/usr/bin/python3

"""
This script takes GitHub username and personal access token as
arguments and uses the GitHub API to display the user ID.
"""

import requests
import sys

def get_user_id(username, token):
    """
    Retrieves the user ID using GitHub API with Basic Authentication
    using the provided username and personal access token.
    """
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        print("Your GitHub User ID:", user_id)

    else:
        print(f"Error: Unable to fetch user ID")

if __name__ == "__main__":

    username = sys.argv[1]
    token = sys.argv[2]
    get_user_id(username, token)
