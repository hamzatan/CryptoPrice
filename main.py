from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import web_hook as web

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'dac2a887-1990-486d-a476-dd8dcf037a61'
}

tickerList = r'/home/htanveer/Documents/tickerList.txt'

# Reads the tickerList file to grab the list of Crypto to search
with open(tickerList, 'r') as file:
    crypto_param_str = file.read()

# URL for API's
# mapURL - Grab CMC ID of the currency
# idURL - Grab ID relevant data from API

map_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
id_url = ' https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

crypto_param_str = crypto_param_str.replace('\n', ',')
crypto_param_str = crypto_param_str[:-1]

parameter_symbol = {'symbol': crypto_param_str}
crypto_names_list = crypto_param_str.split(',')


def api_session(url, parameters):
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data_symbol = json.loads(response.text)
        return data_symbol
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("Error: ", e)


currency_id = api_session(map_url, parameter_symbol)

crypto_id = [currency_id['data'][index]['id'] for index in range(len(crypto_names_list))]
crypto_id_param = (','.join(f'{id_crypto}' for id_crypto in crypto_id))

parameter_id = {'id': crypto_id_param}

currency_price = api_session(id_url, parameter_id)

currency_price_dict = {}

for currency in range(len(crypto_names_list)):
    print("Current price of {} {}".format(crypto_names_list[currency], str(
        currency_price['data'][str(crypto_id[currency])]['quote']['USD']['price'])))
    currency_price_dict[str(crypto_names_list[currency])] = \
        currency_price['data'][str(crypto_id[currency])]['quote']['USD']['price']

if currency_price_dict["BTC"] > 10000:
    print("Price is greater than 10000")
    # web

print(currency_price)
