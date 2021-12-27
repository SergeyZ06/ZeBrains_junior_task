# Module for testing.

import requests
from fake_headers import headers


url = r'http://127.0.0.1:5000//text-recognition'
path_image_1 = r'images/image_1.jpg'
path_image_2 = r'images/image_2.png'
path_image_3 = r'images/image_3.jpg'

with open(file=path_image_1, mode='rb') as image:
    response = requests.request(method='POST', headers=headers.make_header(), url=url, files={'image': image})

print(response.text)
