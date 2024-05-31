import os
import datetime
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from User import User
import pickle

folder_path='Stock_Users'
def fetch_and_save_stock_data(symbol:str, date: datetime.date)->dict:
    # Fetch stock data from Yahoo Finance
    stock_start=(date-datetime.timedelta(days=60)).strftime('%Y-%m-%d')
    stock_end=date.strftime('%Y-%m-%d')
    stock_data = yf.download(symbol, start=stock_start, end=stock_end)
    del stock_data['Adj Close']
    del stock_data['Open']
    del stock_data['Close']
    return stock_data


def get_plots(symbol:str,stock_data: pd.DataFrame) -> dict:
    plots = {}

    # Plot the last week of data
    last_week_data = stock_data[-7:]
    fig_last_week= plt.figure(figsize=(10, 5))
    plt.plot(last_week_data.index, last_week_data['High'], label='High Price')
    plt.plot(last_week_data.index, last_week_data['Low'], label='Low Price')
    plt.title(f'{symbol} Stock Prices - Last Week')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plots['last_week'] = fig_last_week
    plt.close(fig_last_week)

    # Plot the last month of data
    last_month_data = stock_data[-30:]
    fig_last_month = plt.figure(figsize=(10, 5))
    plt.plot(last_month_data.index, last_month_data['High'], label='High Price')
    plt.plot(last_month_data.index, last_month_data['Low'], label='Low Price')
    plt.title(f'{symbol} Stock Prices - Last Month')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plots['last_month'] = fig_last_month
    plt.close(fig_last_month)

    # Plot the last 2 months of data
    last_two_months_data = stock_data[-60:]
    fig_last_two_months = plt.figure(figsize=(10, 5))
    plt.plot(last_two_months_data.index, last_two_months_data['High'], label='High Price')
    plt.plot(last_two_months_data.index, last_two_months_data['Low'], label='Low Price')
    plt.title(f'{symbol} Stock Prices - Last 2 Months')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plots['last_two_months'] = fig_last_two_months
    plt.close(fig_last_two_months)

    return plots

def end_session(currentUser:User):
    '''method saves the user to teh databes- used in relogging and closing the program'''
    dest_path=folder_path+"\\"+currentUser.get_login()
    if os.path.exists(dest_path):
        os.remove(dest_path)
    file=open(dest_path, "ab")
    pickle.dump(currentUser,file)
    file.close()

#fetch_and_save_stock_data('GME',datetime.date(2005,1,1))
#print(fetch_and_save_stock_data('GME',datetime.date(2005,1,8)))
#plots = get_plots('GME',fetch_and_save_stock_data('GME',datetime.date(2005,1,8)))