#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL, and displays the body of the response.
If the HTTP status code is greater than or equal to 400, it prints an error message with the status code.
"""

import requests
import sys

def main():
    """Main function"""
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)

if __name__ == "__main__":
    main()

