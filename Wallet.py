import tkinter as tk
from decimal import Decimal
from tkinter import *
from tkinter import ttk
from User import User
from Transaction import Transaction
import Event
def sell_stock(frame,label,user:User,stock:str,price:Decimal):
    seller=Transaction(user,stock,price,1,frame,label)
    seller.mainloop()
class Wallet(tk.Frame):
    def __init__(self, parent,user:User):
        super().__init__(parent)
        self.user = user
        self.parent = parent

        self.pack(fill=tk.BOTH, expand=1)
        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.wallet=self.user.get_wallet()
        for entry in self.wallet:
            frame = tk.Frame(self.scrollable_frame)
            label = tk.Label(frame, text='Stock:'+entry+" with shares: "+ str(self.wallet[entry]["shares"])+
                             " Paid for stocks: "+ str(self.wallet[entry]["paid"]))
            button1 = tk.Button(frame, text="View stock trend")
            button2 = tk.Button(frame, text="Sell",command=lambda:sell_stock(frame,label,self.user,entry,
                                                                             Event.get_price(entry,self.user.get_date(),1)))

            label.pack(side="left",fill=tk.X, padx=5)
            button1.pack(side="right", padx=5)
            button2.pack(side="right", padx=5)

            frame.pack(fill="x", pady=5)

