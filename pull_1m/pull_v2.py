import pandas
import alpaca_trade_api as tradeapi
import os

# Note: we are getting the keys for this service fron the environment variables
#       This can be re-written to pull values from Hasi's VAULT if desired.  The effect would be the same.

API_KEY = os.environ.get('API_KEY')
API_SECRET = os.environ.get('API_SECRET')

api = tradeapi.REST(API_KEY, API_SECRET, base_url='https://paper-api.alpaca.markets')

# default number of bars is 100, if you ask for more it just gives you more previous bars in sets of 100.
# should expect 390 bars of data on from 1M time frames - assuming a trade occured at each frame.

# api.get_barset is deprecated (see README.md)
# note that data is calculated from "end" backwards. (see README.md)

barset = api.get_barset("LC", timeframe="minute", start='2021-09-09', end='2021-09-10')
bars = barset['LC']

# print(barset)
out = {}
df1 = pandas.DataFrame(out, columns = ['Datetime', 'Open', 'High', 'Low','Close','Volume'])  

# Note: no adjusted close

count = 0
for bar in bars:
    count += 1
    date = {"Datetime": bar.t}
    open = {"Open": bar.o}
    high = {"High": bar.h}
    low = {"Low": bar.l}
    close = {"Close": bar.c}
    volume = {"Volume": bar.v}
    bar = {**date, **open, **high, **low, **close, **volume}
    df1 = df1.append(bar,ignore_index=True)

print("Count:", count)
fname = r"M:\data\out.csv"
print("Writing: ", fname)
df1.to_csv (fname, index = False, header=True)