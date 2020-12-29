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

class Binancer:
    
    api_key=os.environ.get('binance_api')
    api_secret=os.environ.get('binance_secret')
    client=Client(api_key, api_secret)

    # INIT
    def __init__(self):
        api_key=os.environ.get('binance_api')
        api_secret=os.environ.get('binance_secret')
        client=Client(api_key, api_secret)
       
##################################################################################
# GET CONNECTION INFOS
    ## get server time
    def getServerTime(self):
        time_res=self.client.get_server_time()
        return time_res
    ## get system status
    def getSystemStatus(self):
        status=self.client.get_system_status()
        return status
    ## get exchange info
    def getExchangeInfo(self):
        info = self.client.get_exchange_info()
        return info
    ## get symbol info
    def getSymbolInfo (self,sym):
        symbolInfo=self.client.get_symbol_info(sym)
        return symbolInfo


##################################################################################
# ACCOUNT INFOS
    ## get account info -> return dict
    def getAccountInfo(self):
        accountInfo=self.client.get_account()
        return accountInfo
    ## get asset balance
    def getAssetBalance(self,coin):
        balance="asset='"+coin+"'"
        print(balance)
        assetBalance=self.client.get_asset_balance(balance)
        return assetBalance

##################################################################################
# GET PRICES
    def getSymbolTicker(sym):
        ticker=self.client.get_ticker(sym)
        return ticker


# TRADING
    ## fetch all orders
    def fetchAllOrders(self,coin):
        orders=self.client.get_all_orders(symbol=coin, limit=10)
        return orders



