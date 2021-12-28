# Module for testing.

import requests
from fake_headers import headers


url = r'http://127.0.0.1:5000//emotion-detection'
str_text_1 = 'I like you. I love you'
str_text_2 = 'Have a good time!'
str_text_3 = 'Do not do that!'

response = requests.request(method='POST', headers=headers.make_header(), url=url, params={'text': str_text_1})

print(response.text)
