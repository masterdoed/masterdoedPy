import binancePY
from binancePY import Binancer



# MAIN
trader=Binancer()

# Simple function test + examples
#print(trader.getServerTime())
#print(trader.getSystemStatus())
#print(trader.getExchangeInfo())
#print(trader.getSymbolInfo("BTCUSDT"))
#print(trader.getAccountInfo())
print(trader.getAssetBalance("ETH"))
print(trader.getSymbolTicker("ETH"))