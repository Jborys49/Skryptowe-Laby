import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from User import User
import Event
import os
stocks="TEAR,SMA,CABG,UAPH,FSL.B,DRY,SUAI,PRAI,NGD,IWA,SPOK,NP,INPC,AMZGQ,NLC,FENC,ORA,ZIPR,OHAI,CPNO,MPCCQ,MKTX,ATB,USSPQ,MTL,GME.B,LONG,FOXH,DWA,CLMS,BBW,XNNHQ,NRF,GBCS,CUBE,TWGP,SHO,VNUS,BDAY,LOCMQ,JRJC,ICOPQ,GGBMQ,ANSW,TPGI,RTWIQ,ILSE,GKIS,PSBH,INVA,ARCC,ACFC,YMI,PSPT,NVSL,PRSG,CLWA,JOBS,JMDT,CPL,VSCN,TTM,VLLY,EEEE,BECN,SQBGQ,SPSX,BLIBQ,CMNR,STON,KUHM,OCLR,IOC,TSTC"
stocks=stocks.split(",")

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
            button = tk.Button(scrollable_frame, text=stock)
            button.pack(fill=tk.X, padx=5, pady=2)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


