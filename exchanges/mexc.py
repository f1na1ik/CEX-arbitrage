import requests

def get_mexc_prices():
    response = requests.get('https://www.mexc.com/open/api/v2/market/ticker')
    #print(response)
    data = response.json()
    prices = {}
    for item in data['data']:
        symbol = item['symbol'].replace('_', '')
        volume = item['amount']
        price = item['last']
        #print(symbol, volume, price)
        if symbol.endswith('USDT') and '3L' not in symbol and '3S' not in symbol:
            prices[symbol] = float(price)
    #print(prices)
    return prices

get_mexc_prices()