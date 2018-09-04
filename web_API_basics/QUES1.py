import requests
response=requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
import json
data=response.json()
print(data["quoteText"])