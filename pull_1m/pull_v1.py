import alpaca_trade_api as tradeapi
import os

API_KEY = os.environ.get('API_KEY')
API_SECRET = os.environ.get('API_SECRET')

api = tradeapi.REST(API_KEY, API_SECRET, base_url='https://paper-api.alpaca.markets')

# Get daily price data for AAPL over the last 5 trading days.
barset = api.get_barset('ILMN', 'day', limit=1, start='2021-02-12', end='2021-02-13')
stock = barset['ILMN']

print("  open:", stock[0].o)
print("  high:", stock[0].h)
print("   low:", stock[0].l)
print(" close:", stock[-1].c)
print("volume:", stock[0].v)