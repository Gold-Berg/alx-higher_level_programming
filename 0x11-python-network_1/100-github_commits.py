#!/usr/bin/env python3
"""
This script lists 10 commits (from the most recent to oldest) of a repository by a specific user.
"""

import requests
import sys

def get_commits(owner, repo):
    """Retrieve 10 commits of the repository by the user"""
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {'per_page': 10}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Unable to fetch commits. Status code: {response.status_code}")

def main():
    """Main function"""
    if len(sys.argv) != 3:
        print("Usage: {} <repository> <owner>".format(sys.argv[0]))
        sys.exit(1)

    repo = sys.argv[1]
    owner = sys.argv[2]

    get_commits(owner, repo)

if __name__ == "__main__":
    main()
