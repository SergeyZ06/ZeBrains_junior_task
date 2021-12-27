# Module for testing.

import requests
from fake_headers import headers


url = r'http://127.0.0.1:5000//similar-recognition'
text_1 = r"At eight o'clock on Thursday morning Arthur didn't feel very good."
text_2 = r"At eight o'clock on Thursday morning David didn't feel very good."

response = requests.request(method='POST', headers=headers.make_header(), url=url,
                            params={'text_1': text_1,
                                    'text_2': text_2})

print(response.text)
