import json
import sys
from bittrex.bittrex import Bittrex


my_bittrex = Bittrex(None, None)
my_markets=["USD-BTC","USD-ETH","BTC-XVG","BTC-NXS"]

for market in my_markets:
    market_dict=my_bittrex.get_market_summary(market)["result"]
    print market_dict[0]["TimeStamp"],"   |   ", market_dict[0]["MarketName"],"   |   ",market_dict[0]["Last"]
    print "---------------------------------------------------------------------------------------"
