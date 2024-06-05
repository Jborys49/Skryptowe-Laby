import os
import datetime
import yfinance as yf
from decimal import Decimal
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pickle
import pandas as pd

from User import User

folder_path='Stock_Users'
def fetch_and_save_stock_data(symbol:str, date: datetime.date)->tuple[pd.DataFrame,int]:
    '''Method fetches data untill given date from yfinance for further use'''
    # Fetch stock data from Yahoo Finance
    stock_start=(date-datetime.timedelta(days=60))
    stock_end=(date+datetime.timedelta(days=1))
    stock_data = yf.download(symbol, start=stock_start, end=stock_end)
    del stock_data['Adj Close']
    del stock_data['Open']
    del stock_data['Close']
    last_volume=stock_data['Volume'].tail(1).iloc[0]
    del stock_data['Volume']
    return stock_data,last_volume

def plot_stock(symbol:str, stock_data: pd.DataFrame):
    '''get the 3 availible stock plots provided by the program'''
    if not os.path.isfile(os.path.join('Stock_Graphs/',symbol + '2m.png')):
        get_plots('Stock_Graphs/' + symbol + '2m.png',stock_data)
        get_plots('Stock_Graphs/' + symbol + '1m.png', stock_data.tail(30))
        get_plots('Stock_Graphs/' + symbol + '1w.png', stock_data.tail(7))

def get_plots(file_path:str,stock_data: pd.DataFrame):
    '''Create a plot from given dataframe and save it to given location'''
    plt.figure(figsize=(6,4))
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
    plt.savefig(file_path)
    plt.close()


def save_user(currentUser:User):
    '''method saves the user to teh databes- used in relogging and closing the program'''
    dest_path=folder_path+"\\"+currentUser.get_login()
    if os.path.exists(dest_path):
        os.remove(dest_path)
    file=open(dest_path, "ab")
    pickle.dump(currentUser,file)
    file.close()
def get_price(stock:str,date:datetime.date,type:int)->Decimal:
    '''method gets the price of given stock,0 for buying(High) 1 for selling(Low)'''
    if type==0:
        price=yf.download(stock, start=(date-datetime.timedelta(days=7)), end=(date+datetime.timedelta(days=1)))
        price=price['High'][-1]
    else:
        price = yf.download(stock, start=(date-datetime.timedelta(days=7)), end=(date + datetime.timedelta(days=1)))
        price=price['Low'][-1]
    return Decimal(price).quantize(Decimal('1.00'))

def clean_pdf():
    for file in os.listdir('Stock_Graphs'):
        os.unlink(os.path.join('Stock_Graphs', file))