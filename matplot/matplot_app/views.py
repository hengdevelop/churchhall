from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64

import pandas as pd
import numpy as np
import yfinance as yf
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

def home(request):
    #plt.plot(range(10))

    tickerStrings = ['NDQ.AX', 'WOW.AX']
    df_list = list()
    for ticker in tickerStrings:
        data = yf.download(ticker, group_by="Ticker", period='180d')
        data['ticker'] = ticker  # add this column becasue the dataframe doesn't contain a column with the ticker
        df_list.append(data)

    # combine all dataframes into a single dataframe
    df = pd.concat(df_list)

    print(df.head())
    df2 = df[df.ticker == 'NDQ.AX']['Low']
    df3 = df[df.ticker == 'WOW.AX']['Low']
    #df2.plot()
    fig = plt.figure(figsize=(20, 10))
    #fig = plt.gcf()


    x = np.arange(0,4*np.pi,0.1)

    y = np.sin(x)

    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Vertically stacked subplots')
    ax1.plot(df2.index, df2)

    date_form = DateFormatter("%m-%y")




    ax1.set_xticklabels(df2.index, rotation=30, ha='right', Fontsize =8)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m'))
    #ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')
    #ax2.plot(x, y)
    ax2.plot(df3.index, df3)
    ax2.set_xticklabels(df3.index, rotation=30, ha='right', Fontsize =8)
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m'))

    #ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
    #plt.plot(x,y)
    #plt.plot(df2.index, df2)
    print(df2)
    print ("index")
    print(df2.index)
    #plt.plot(df[0], df[1])
    #fig = df2.plot()
    fig = plt.gcf()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'home.html', {'data':uri})

# Create your views here.
