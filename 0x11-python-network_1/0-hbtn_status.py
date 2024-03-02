#!/usr/bin/env python3
""" Python script that fetches https://intranet.hbtn.io/status """
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body_response = response.read()
    print("Body response:")
    print("\t- type:", type(body_response))
    print("\t- content:", body_response)
    print("\t- utf8 content:", body_response.decode('utf-8'))

