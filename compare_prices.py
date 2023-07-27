from exchanges.binance import get_binance_prices
from exchanges.mexc import get_mexc_prices

def compare_prices():
    binance_prices = get_binance_prices()
    mexc_prices = get_mexc_prices()

    differences = {}
    print(binance_prices)
    print(mexc_prices)
    for symbol in binance_prices:
        if symbol in mexc_prices:
            binance_price = binance_prices[symbol]
            print(binance_price)
            mexc_price = mexc_prices[symbol]
            print(mexc_price)
            difference = binance_price - mexc_price
            #print(symbol, difference)

print(compare_prices())