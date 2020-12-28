import os
from binance.client import Client

# PREREQUISITES ON MACOS
#XCode + XCode command line tools
#brew install pyenv
#pyenv install 3.9.0
#pyenv global 3.9.0
#pyenv version
#pip install python-binance
#sudo python -m pip install python-binance
#export binance_api="your_api_key_here"
#export binance_secret="your_api_secret_here"

# INIT
api_key=os.environ.get('binance_api')
api_secret=os.environ.get('binance_secret')
client=Client(api_key, api_secret)

# GET CONNECTION INFOS
## get server time
def getServerTime():
    time_res=client.get_server_time()
    return time_res
## get system status
def getSystemStatus():
    status=client.get_system_status()
    return status
## get exchange info
def getExchangeInfo():
    info = client.get_exchange_info()
    return info
## get symbol info
def getSymbolInfo (sym):
    symbolInfo=client.get_symbol_info(sym)
    return symbolInfo

# ACCOUNT INFOS
## get account info
def getAccountInfo():
    info=client.get_account()
    return account
## get asset balance
def getAssetBalance(coin):
    balance=client.get_asset_balance(asset='BTC')
    return asset




# GET TICKERS
def getSymbolTicker(*symbol):
    ticker=client.get_ticker(symbol)
    print(ticker)
    return ticker


# TRADING
## fetch all orders
def fetchAllOrders(coin):
    orders=client.get_all_orders(symbol=coin, limit=10)
    return orders







# MAIN
print(getSystemStatus())

getSymbolTicker("BTCUSDT")
