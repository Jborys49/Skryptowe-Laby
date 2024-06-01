import tkinter as tk
from decimal import Decimal
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from User import User
from StockDetails import StockDetails
import Event
import os

class Wallet(tk.Frame):
    def __init__(self, parent,user:User):
        super().__init__(parent)
        self.user = user

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
                             " Price: "+ str(self.wallet[entry]["paid"]))
            button1 = tk.Button(frame, text="View stock trend")
            button2 = tk.Button(frame, text="Sell")

            label.pack(side="left", padx=5)
            button1.pack(side="left", padx=5)
            button2.pack(side="left", padx=5)

            frame.pack(fill="x", pady=5)

'''inet=tk.Tk()
tester=User('bingo','bango',Decimal(200.0))
tester.purchase('GOOG',Decimal(2.97),10)
tester.purchase('GOOa',Decimal(0.01),10)
tester.purchase('GOOb',Decimal(0.01),10)
tester.purchase('GOOc',Decimal(0.01),10)
tester.purchase('GOOd',Decimal(0.01),10)
tester.purchase('GOOG',Decimal(0.01),10)
tester.purchase('GOOe',Decimal(0.01),10)
tester.purchase('GOOf',Decimal(0.01),10)
tester.purchase('GOOG1',Decimal(2.97),10)
tester.purchase('GOOa1',Decimal(0.01),10)
tester.purchase('GOOb1',Decimal(0.01),10)
tester.purchase('GOOc1',Decimal(0.01),10)
tester.purchase('GOOd1',Decimal(0.01),10)
tester.purchase('GOOG1',Decimal(0.01),10)
tester.purchase('GOOe1',Decimal(0.01),10)
tester.purchase('GOOf1',Decimal(0.01),10)
bruh=Wallet(inet,tester).pack()
inet.mainloop()'''