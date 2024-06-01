import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from User import User
from StockDetails import StockDetails
import Event
import os
stocks="AAPL,MSFT,GOOG,AMZN,JNJ,WMT,JPM,PG,XOM,T,HD,DIS,BAC,VZ,INTC,KO,CSCO,MRK,CVX,ORCL,ABT,NKE,MCD,IBM,MMM,CAT,UNH,HON,C,GE,DE,CL,MO,AXP,USB,GS,PFE,WFC,BMY,SBUX,TXN,SYY,MDT,QCOM,LLY,UPS,MS,DHR,TGT,COST,CVS,LMT,ADP,ISRG,SCHW,SPGI,ITW,RTN,NSC,AMGN,GILD,JCI,GPC,AFL,BDX,CSX,EMR,BEN,TROW,COF,FIS,AON,KMB,ADM,AMT,BK,FDX,EMN"
stocks=stocks.split(",")

def get_stock_details(frame: tk.Frame, user: User,stock:str):
    for widget in frame.winfo_children():
        widget.destroy()
    StockDetails(frame,user,stock).pack(fill=tk.BOTH,expand=1)
class BuyScreen(tk.Frame):
    def __init__(self, parent,user:User):
        super().__init__(parent)
        self.user=user


        # Create the main frame to hold the left and right frames
        main_frame = tk.Frame(self)
        main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create the left frame with a scrollable list of buttons
        left_frame = tk.Frame(main_frame, width=90)
        left_frame.pack_propagate(0)
        left_frame.pack(side=tk.LEFT,fill=tk.Y)

        # Create the right frame to fill the rest of the interface
        right_frame = tk.Frame(main_frame, bg="white")
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(left_frame)
        scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for stock in stocks:
            button = tk.Button(scrollable_frame, text=stock,command=
            lambda stc=stock:get_stock_details(right_frame,self.user,stc))
            button.pack(fill=tk.X, padx=5, pady=2)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

