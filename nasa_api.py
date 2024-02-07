#!/usr/bin/python3
# create earht view app using NASA API

import requests

response = requests.get("https://httpbin.org/")

res_json = response.json()
# del res_json['origin']
print(res_json)