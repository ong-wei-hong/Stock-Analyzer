import pandas as pd
import numpy as np
import yfinance as yf
import datetime  as dt
from pandas_datareader import data as pdr
yf.pdr_override()

stock=input("Ticker: ")
print(stock)

df=pdr.get_data_yahoo(stock)

ma=250

smaString="Sma_"+str(ma)
df[smaString]=df.iloc[:, 4].rolling(window=ma).mean()

print(df) 

ans=0

for i in df.index:
    if(df[smaString][i]):
        temp=(df["Close"][i]-df[Sma_250][i])/df[Sma_250]
        if(temp<ans):
            ans=temp

print(ans)
