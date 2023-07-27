import requests

def get_binance_prices():
    response = requests.get('https://api.binance.com/api/v3/ticker/price')
    data = response.json()

    prices = {}
    for item in data:
        symbol = item['symbol']
        if symbol.endswith('USDT') and 'UP' not in symbol and 'DOWN' not in symbol:
            price = item['price']
            #print(symbol, price)
            prices[symbol] = float(price)
    return prices


get_binance_prices()