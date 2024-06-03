import tkinter as tk
import customtkinter as ctk
from decimal import Decimal

from User import User
from ErrorPopup import ErrorPopup

def buy(master:ctk.CTk,user:User,name:str,price:Decimal, nr_of_shares:str):
    '''Method updates user with stocks, invokes ErrorPopup if funds insufficient'''
    nr_of_shares=int(nr_of_shares)
    if user.purchase(name,price,nr_of_shares):
        master.destroy()
    else:
        error=ErrorPopup('Not enough Funds to sell')
def sell(master:ctk.CTk,user:User,stock:str,price:Decimal, nr_of_shares:str,sell_frame:ctk.CTkFrame,label:ctk.CTkLabel):
    '''Method updates user with funds, invokes ErrorPopup if stock insufficient'''
    nr_of_shares=int(nr_of_shares)
    if user.sell(stock,price,nr_of_shares):
        if stock in user.get_wallet():
            label.configure(text='Stock:'+stock+" with shares: "+ str(user.get_wallet()[stock]["shares"])+
                             " Paid for stocks: "+ str(user.get_wallet()[stock]["paid"]))
        else:
            sell_frame.destroy()
        master.destroy()
    else:
        error=ErrorPopup('Not enough stock ot sell')
class Transaction(ctk.CTk):
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
            intro=ctk.CTkLabel(self,text="You are buying "+self.stock)
            intro.pack()
            details=ctk.CTkLabel(self,text="Current price of the stock: "+str(self.price.quantize(Decimal('1.00'))))
            details.pack()
            funds=ctk.CTkLabel(self,text="Your current funds: "+str(self.user.get_current_funds()))
            funds.pack()
            action=ctk.CTkLabel(self,text="How many stocks would you like to buy")
            action.pack()
            determiner=ctk.CTkEntry(self)
            determiner.pack()
            commence=ctk.CTkButton(self,text="BUY",command=lambda:buy(self,self.user,self.stock,self.price,determiner.get()))
            commence.pack()
        else:
            self.title('Selling confirmation')
            intro = ctk.CTkLabel(self, text="You are selling " + self.stock)
            intro.pack()
            details = ctk.CTkLabel(self, text="Current price of the stock: " + str(self.price.quantize(Decimal('1.00'))))
            details.pack()
            funds = ctk.CTkLabel(self, text="Your stock number: " + str(self.user.get_number_of_stock(self.stock)))
            funds.pack()
            action = ctk.CTkLabel(self, text="How many stocks would you like to sell")
            action.pack()
            determiner = ctk.CTkEntry(self)
            determiner.pack()
            commence = ctk.CTkButton(self, text="SELL",command=lambda:sell(self,self.user,self.stock,self.price,determiner.get(),sell_frame,label))
            commence.pack()
