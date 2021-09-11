import alpaca_trade_api as tradeapi

# update 9/4/2021 11:24 AM.  Future version will be setup to pull keys from either environment or from HashiCorp vault.
# this certainly represents why one needs to be careful when commiting code to a repository

api = tradeapi.REST('x', 'x', base_url='https://paper-api.alpaca.markets')

# Get daily price data for AAPL over the last 5 trading days.
barset = api.get_barset('ILMN', 'day', limit=1, start='2021-02-12', end='2021-02-13')
stock = barset['ILMN']

print("  open:", stock[0].o)
print("  high:", stock[0].h)
print("   low:", stock[0].l)
print(" close:", stock[-1].c)
print("volume:", stock[0].v)
