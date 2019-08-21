from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'dac2a887-1990-486d-a476-dd8dcf037a61'
}

tickerList = r'/home/htanveer/Documents/tickerList.txt'
cryptoTicker = []

with open(tickerList, 'r') as file:
    cryptoTicker = file.read()

print("CryptoPrice is running...")
mapurl = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
idurl = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
session = Session()
session.headers.update(headers)
idData = ''

try:
    parameters = ''
    for items in cryptoTicker:
        parameters += ','.join(items)

    response = session.get(mapurl, param=parameters)
    data = json.loads(response.text)
    for outdata in data[data]:
        idData = ','.join(outdata)

    response = session.get(idurl, param=parameters)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    pass

