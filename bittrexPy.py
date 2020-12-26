import json
import sys
import os
from bittrex.bittrex import Bittrex


my_bittrex = Bittrex(None, None)
my_markets=["USD-BTC","USD-ETH","BTC-XVG","BTC-NXS", "USD-ADA", "USD-XRP", "BTC-EMC2","BTC-LTC"]

for market in my_markets:
    market_dict=my_bittrex.get_market_summary(market)["result"]
    
    if market_dict[0]["MarketName"]=="USD-BTC":
        if market_dict[0]["Last"] < 23800:
            os.system("say 'Bitcoin is going down'")
        elif market_dict[0]["Last"] > 24500:
            os.system("say 'Bitcoin is above 24500'")
        elif market_dict[0]["Last"] > 25000:
            os.system("say 'Bitcoin is above 25000'")
        elif market_dict[0]["Last"] < 24000:
            os.system("say 'Bitcoin is below 24000'")



    print market_dict[0]["TimeStamp"],"   |   ", market_dict[0]["MarketName"],"   |   ",market_dict[0]["Last"]
    print "---------------------------------------------------------------------------------------"
