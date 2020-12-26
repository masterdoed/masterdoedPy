import os

from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor



# init
#export binance_api="your_api_key_here"
#export binance_secret="your_api_secret_here"
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)
btc_price = {'error':False}


def btc_trade_history(msg):
    ''' define how to process incoming WebSocket messages '''
    if msg['e'] != 'error':
        print(msg['c'])
        btc_price['last'] = msg['c']
        btc_price['bid'] = msg['b']
        btc_price['last'] = msg['a']
    else:
        btc_price['error'] = True



# get latest price from Binance API
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")

# print full output (dictionary)
print(btc_price)
print(btc_price["price"])


