#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token) and uses the GitHub API to display your id.
"""

import requests
import sys

def get_github_id(username, token):
    """Retrieve GitHub user ID"""
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        return response.json().get('id')
    else:
        return None

def main():
    """Main function"""
    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    github_id = get_github_id(username, token)
    print(github_id)

if __name__ == "__main__":
    main()

