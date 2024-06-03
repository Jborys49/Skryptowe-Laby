import tkinter as tk
import customtkinter as ctk
from tkinter import ttk

from User import User
from StockDetails import StockDetails

stocks="AAPL,MSFT,GOOG,AMZN,JNJ,WMT,JPM,PG,XOM,T,HD,DIS,BAC,VZ,INTC,KO,CSCO,MRK,CVX,ORCL,ABT,NKE,MCD,IBM,MMM,CAT,UNH,HON,C,GE,DE,CL,MO,AXP,USB,GS,PFE,WFC,BMY,SBUX,TXN,SYY,MDT,QCOM,LLY,UPS,MS,DHR,TGT,COST,CVS,LMT,ADP,ISRG,SCHW,SPGI,ITW,RTN,NSC,AMGN,GILD,JCI,GPC,AFL,BDX,CSX,EMR,BEN,TROW,COF,FIS,AON,KMB,ADM,AMT,BK,FDX,EMN"
stocks=stocks.split(",")

def get_stock_details(frame: ctk.CTkFrame, user: User,stock:str):
    for widget in frame.winfo_children():
        widget.destroy()
    StockDetails(frame,user,stock).pack(fill=ctk.BOTH,expand=1)
class BuyScreen(ctk.CTkFrame):
    def __init__(self, parent,user:User):
        super().__init__(parent)
        self.user=user


        # Create the main frame to hold the left and right frames
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

        # Create the left frame with a scrollable list of buttons
        left_frame = ctk.CTkFrame(main_frame, width=90)
        left_frame.pack_propagate(False)
        left_frame.pack(side=ctk.LEFT,fill=ctk.Y)

        # Create the right frame to fill the rest of the interface
        right_frame = ctk.CTkFrame(main_frame)
        right_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

        canvas = ctk.CTkCanvas(left_frame)
        scrollbar = ctk.CTkScrollbar(left_frame, command=canvas.yview)
        scrollable_frame = ctk.CTkFrame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for stock in stocks:
            button = ctk.CTkButton(scrollable_frame, text=stock,width=5,command=
            lambda stc=stock:get_stock_details(right_frame,self.user,stc))
            button.pack(fill=ctk.X, padx=5, pady=2)

        scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)
        canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

