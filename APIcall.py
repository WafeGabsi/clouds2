
import dotenv
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")
url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY ,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  for i in data['data']:
    print("id "+str(i['id'])+"\n")
    print("quote"+ str(i['quote'])+"\n")
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)