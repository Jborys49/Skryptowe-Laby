import tkinter as tk
from decimal import Decimal

from User import User


def buy(master:tk.Tk,user:User,name:str,price:Decimal, nr_of_shares:str):
    nr_of_shares=int(nr_of_shares)
    if user.purchase(name,price,nr_of_shares):
        master.destroy()
    else:
        error=tk.Tk()
        error.minsize(200,100)
        tk.Label(error,text="Funds Insufficient!").pack()
        tk.Button(error,text="OK",command=lambda:error.destroy()).pack()
def sell(master:tk.Tk,user:User,stock:str,price:Decimal, nr_of_shares:str,sell_frame:tk.Frame,label:tk.Label):
    nr_of_shares=int(nr_of_shares)
    if user.sell(stock,price,nr_of_shares):
        if stock in user.get_wallet():
            label.config(text='Stock:'+stock+" with shares: "+ str(user.get_wallet()[stock]["shares"])+
                             " Paid for stocks: "+ str(user.get_wallet()[stock]["paid"]))
        else:
            sell_frame.destroy()
        master.destroy()
    else:
        error=tk.Tk()
        error.minsize(200,100)
        tk.Label(error,text="Not Enough Stock!").pack()
        tk.Button(error,text="OK",command=lambda:error.destroy()).pack()
class Transaction(tk.Tk):
    '''class that handles transactions (buying and selling)
     0 type is a buy transaction and 1 type is a selling transaction'''
    def __init__(self,user:User,stock:str,price:Decimal,type:int,sell_frame=None,label=None):
        super().__init__()
        self.user=user
        self.minsize(200,100)
        self.price=price
        self.stock=stock
        if type==0:
            self.title('Buying confirmation')
            intro=tk.Label(self,text="You are buying "+self.stock)
            intro.pack()
            details=tk.Label(self,text="Current price of the stock: "+str(self.price.quantize(Decimal('1.00'))))
            details.pack()
            funds=tk.Label(self,text="Your current funds: "+str(self.user.get_current_funds()))
            funds.pack()
            action=tk.Label(self,text="How many stocks would you like to buy")
            action.pack()
            determiner=tk.Entry(self)
            determiner.pack()
            commence=tk.Button(self,text="BUY",command=lambda:buy(self,self.user,self.stock,self.price,determiner.get()))
            commence.pack()
        else:
            self.title('Selling confirmation')
            intro = tk.Label(self, text="You are selling " + self.stock)
            intro.pack()
            details = tk.Label(self, text="Current price of the stock: " + str(self.price.quantize(Decimal('1.00'))))
            details.pack()
            funds = tk.Label(self, text="Your stock number: " + str(self.user.get_number_of_stock(self.stock)))
            funds.pack()
            action = tk.Label(self, text="How many stocks would you like to sell")
            action.pack()
            determiner = tk.Entry(self)
            determiner.pack()
            commence = tk.Button(self, text="SELL",command=lambda:sell(self,self.user,self.stock,self.price,determiner.get(),sell_frame,label))
            commence.pack()
