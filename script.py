from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv 
import numpy as np
import pandas as pd

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'ae9e398b-710d-4c5b-8e0b-9747d61707a2',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  # save to json
  jsondata = json.dumps(data)
  f = open("data.json","w")
  f.write(jsondata)
  f.close()
  # # save to plain txt
  # f = open("textdata.txt","w")
  # f.write(str(data))
  # f.close()
  # # save to csv 
  # csvdata = csv.writer(open("csvdata.csv","w"))
  # for key, val in data.items():
  #     csvdata.writerow([key,val])
#   print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)