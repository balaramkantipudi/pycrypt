# Imports
import os
from binance import Client
from dotenv import load_dotenv
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# Load secrets
load_dotenv()
API_KEY = os.getenv('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

# Init client
client = Client(API_KEY,SECRET_KEY)

# Test connection
if (client.get_account()): print("==> Connected!")
else: print("==> Error: Couldn't connect.")

## Get price data

# By minute
def getMinuteData(symbol, interval, period):
    print("\n==> Fetching data for " + symbol + "...")
    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, period + ' min ago UTC'))
    frame = frame.iloc[:,:6]
    # Name columns
    frame.columns = ['Time','Open','High','Low','Close','Volume']
    # Use timestamps
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    # Transform strings to floats
    frame = frame.astype(float)
    # Return frame
    return frame

def getHourData(symbol, interval, period):
    return ""

def getDayData(symbol, interval, period):
    return ""

## Graphing data

# Save to file
def graphToFile(fig, path, ext):
    print("\n==> Saving data to file...\n")
    fig.get_figure().savefig(path + "." + ext)
    return "==> Saved data to " + path + "." + ext

# Print to terminal

#btc = getMinuteData('BTCUSDT', '1m', '30')
#print(graphToFile(btc.Open.plot(), 'test', 'png'))

# Print price data
#print(getminutedata('BTCUSDT', '1m', '30'))

## Init trading WIP WIP WIP

# Buy if asset falls by more than 0.2%
# Sell if asset rises by more than 0.15% (due to trading fees) OR price falls further by 0.5%

def strategyTest(symbol, qty, done=False):
    # DataFrame of specified symbol
    df = getMinuteData(symbol, '1m', '30')
    # Cumulative returns
    cumulret = (df.Open.pct_change() + 1).cumprod() - 1

    if not done:
        # If falls .2%
        if cumulret[-1] < -0.002
            # Exec order using API
            #order = client.create_order(symbol=symbol, side='BUY', type='MARKET', quantity=qty)
            # Print order
            print("==> Test order completed, params " + symbol + " " + qty + " BUY MARKET") #print(order)
            # Order is done
            done = True
        else:
            print("==> No trade has been executed")
    # Check performance every min
    if done:
        while True:
            df = getMinuteData(symbol, '1m', '30')
            sinceBuy = df.loc[df.index > pd.to_datetime(order['transactTime'], unit='ms')]
            # Check for data, since it only exists in 1m intervals
            if len(sinceBuy) > 0:
                sinceBuyRet = (sinceBuy.Open.pct_change() + 1).cumprod() - 1
                # If falls .15%
                if sinceBuyRet[-1] > 0.0015 or sinceBuyRet[-1] < -0.0015:
                    # Exec sell order using API
                    #order = client.create_order(symbol=symbol, side='SELL', type='MARKET', quantity=qty)
                    print("==> Test sell order completed, params " + symbol + " " + qty + " SELL MARKET") #print(order)
                    # Break while loop
                    break
