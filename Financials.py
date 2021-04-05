import pandas as pd
import numpy as np
import yfinance as yf
import datetime  as dt
from pandas_datareader import data as pdr
yf.pdr_override()

stock=input("Ticker: ")
ticker=yf.Ticker(stock)
print("\n" + ticker.info['longName'] + " (" + ticker.info['symbol'] + ")")
print("\nYearly Financials")

df=ticker.financials
date=[0, 1, 2, 3]
revenue=[0, 1, 2, 3]
income=[0, 1, 2, 3]
index=0

for i in df:
    date[index]=i
    revenue[index]=df[i]["Total Revenue"]
    income[index]=df[i]["Net Income"]
    index+=1

print(df)

#calculate avg revenue growth
avgRevenueGrowth=0
#calculate revenue growth for each year first
for i in range(0, index-1):
    avgRevenueGrowth+=(revenue[i]-revenue[i+1])/revenue[i+1]
        
avgRevenueGrowth/=(index-1)/100
print("\nAverage Revenue Growth =", avgRevenueGrowth, "%")

#caculate net income margin over revenue
avgIncomeMargin=0
#calculate for each year first
for i in range(0, index):
    avgIncomeMargin+=(income[i]/revenue[i])
    
avgIncomeMargin/=index/100
print("Average Income Margin =", avgIncomeMargin, "%")
print("Sum of Average Revenue Growth and Average Income Margin =", avgRevenueGrowth+avgIncomeMargin, "%")

#repeat for quarterly
print("\nQuarterly Financials")

df=ticker.quarterly_financials

index=0
for i in df:
    date[index]=i
    revenue[index]=df[i]["Total Revenue"]
    income[index]=df[i]["Net Income"]
    index+=1

print(df)

#calculate avg revenue growth
#calculate revenue growth for each year first
avgRevenueGrowth=0
for i in range(0, index-1):
    avgRevenueGrowth+=(revenue[i]-revenue[i+1])/revenue[i+1]
    
avgRevenueGrowth/=(index-1)/100
print("\nAverage Revenue Growth =", avgRevenueGrowth, "%")

#caculate net income margin over revenue
#calculate for each year first
avgIncomeMargin=0
for i in range(0, index):
    avgIncomeMargin=(income[i]/revenue[i])
    
avgIncomeMargin/=index/100
print("Average Income Margin =", avgIncomeMargin, "%")
print("Sum of Average Revenue Growth and Average Income Margin =", avgRevenueGrowth+avgIncomeMargin, "%")
