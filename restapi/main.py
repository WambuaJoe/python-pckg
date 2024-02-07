#!/usr/bin/python3
#

import requests

# payload = {'username': 'joe', 'password': 'tests'}
req = requests.get('https://httpbin.org/basic-auth/joe/mand3vu', auth=('joe',
                                                                       'mand3vu'))
print()
print(req.text)
print()