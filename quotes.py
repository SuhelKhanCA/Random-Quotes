# Integrating Random-quotes API into eConnect Project

import requests

url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
response = requests.get(url)

data  = response.json() # Dictionary

data_body = data["data"]
quote = data_body["content"]
author = data_body["author"]

print(quote)
print(author)