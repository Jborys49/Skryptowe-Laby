import os
import datetime
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from User import User
import pickle
import pandas as pd

folder_path='Stock_Users'
def fetch_and_save_stock_data(symbol:str, date: datetime.date)->tuple[pd.DataFrame,int]:
    # Fetch stock data from Yahoo Finance
    stock_start=(date-datetime.timedelta(days=60))
    stock_end=(date+datetime.timedelta(days=1))
    stock_data = yf.download(symbol, start=stock_start, end=stock_end)
    del stock_data['Adj Close']
    del stock_data['Open']
    del stock_data['Close']
    last_volume=stock_data['Volume'].tail(1)
    del stock_data['Volume']
    return stock_data,last_volume


def get_plots(symbol:str,stock_data: pd.DataFrame):
    plt.plot(stock_data.index, stock_data['High'], label='High Prices', color='blue')

    # Plot low prices
    plt.plot(stock_data.index, stock_data['Low'], label='Low Prices', color='red')

    # Set title and labels
    plt.xlabel('Date')
    plt.ylabel('Price')
    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))  # Major ticks on Mondays
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format dates

    # Rotate date labels for better readability
    plt.xticks(rotation=45,fontsize=6)
    # Add legend
    plt.legend()

    # Show the plot
    plt.savefig('Stock_Graphs/'+symbol+'2m.png')


def end_session(currentUser:User):
    '''method saves the user to teh databes- used in relogging and closing the program'''
    dest_path=folder_path+"\\"+currentUser.get_login()
    if os.path.exists(dest_path):
        os.remove(dest_path)
    file=open(dest_path, "ab")
    pickle.dump(currentUser,file)
    file.close()

#fetch_and_save_stock_data('GME',datetime.date(2005,1,1))
bingo,bango=fetch_and_save_stock_data('GME',datetime.date(2005,1,6))
#print(bingo)
get_plots('GME',bingo)
print('bruh')
#plots = get_plots('GME',fetch_and_save_stock_data('GME',datetime.date(2005,1,8)))