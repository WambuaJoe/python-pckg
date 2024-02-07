#!/usr/bin/python3
# create earht view app using NASA API

import requests

headers = {
    "User-Agent": "https://www2.thepiratebay3.to/",
    "Accept": "image/png"
}
response = requests.get("https://httpbin.org/Image  ",
                        headers=headers)

print()
with open("newImg.png", "wb") as fileObj:
    fileObj.write(response.content)
