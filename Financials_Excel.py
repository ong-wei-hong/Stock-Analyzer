import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
yf.pdr_override()

stock=input("Ticker: ")
ticker=yf.Ticker(stock)

df1=ticker.financials
df2=ticker.balance_sheet

#get dates
numDates=0
for i in df1.columns: #get number of dates
    numDates+=1
dates=np.empty(numDates, dtype=object)
for i in range(numDates):
    dates[i]=df1.columns[i]

#initialize data with 1 row first (Gross Profit)
data=pd.DataFrame(index=["Gross Profit"])
for date in dates:
    data[date]=df1[date]["Gross Profit"]

#add rows from df1 (Total Revenue, NIACS)
for i in ["Total Revenue", "Net Income Applicable To Common Shares"]: #df[date][i]
    row=[0 for date in dates]
    index=0
    for date in dates:
        row[index]=df1[date][i]
        index+=1
    data.loc[i]=row

#add rows from df2 (Total Stockholder Equity, Short Long Term Debt, Long Term Debt)
for i in ["Total Stockholder Equity", "Short Long Term Debt", "Long Term Debt"]:
    row=[0 for date in dates]
    index=0
    for date in dates:
        row[index]=df2[date][i]
        index+=1
    data.loc[i]=row

#calculate Gross Margin and NIACS/Revenue
for i in [[0, 1, "Gross Margin"], [2, 1, "NIACS / Revenue"]]: 
    row=[0 for date in dates]
    index=0
    for date in dates:
        row[index]=data[date][i[0]]/data[date][i[1]]
        index+=1
    data.loc[i[2]]=row

#calculate Revenue Growth and NIACS Growth
for i in [[1, "Revenue Growth"], [2, "NIACS Growth"]]:
    row=["NaN" for date in dates]
    for j in range(0, 3):
        row[j]=(data[dates[j]][i[0]]/data[dates[j+1]][i[0]])-1
    data.loc[i[1]]=row

#calculate Total Debt
row=[0 for date in dates]
index=0
for date in dates:
    row[index]=data[date][4]+data[date][5]
    index+=1
data.loc["Total Debt"]=row

#calculate Total Debt to Equity Ratio
row=[0 for date in dates]
index=0
for date in dates:
    row[index]=data[date][10]/data[date][3]
    index+=1
data.loc["Debt to Equity"]=row

data.to_excel(stock + "_Financials.xlsx")
print("saved info to " + stock + "_Financials.xlsx")

