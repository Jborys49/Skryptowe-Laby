import time
import tkinter as tk
import yfinance as yf
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from User import User
from PasswordChager import PasswordChager
from Transaction import Transaction
from decimal import Decimal
import Event
import os

def change_password(user: User):
    pswd = PasswordChager(user)
    pswd.mainloop()
class Profile(tk.Frame):
    def __init__(self,parent,user:User):
        super().__init__(parent)
        self.user=user
        self.icon=ImageTk.PhotoImage(Image.open('Program_Icons/userPic.png').resize((100,100)))

        # Configure grid layout for the main frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)  # Give more weight to bottom frame
        self.grid_columnconfigure(0, weight=1)

        # Top frame (20% of the space)
        top_frame = tk.Frame(self)
        top_frame.configure(background="light green")
        top_frame.grid(row=0, column=0, sticky="nsew")

        label_top = tk.Label(top_frame, text=user.get_login())
        label_top.configure(font=("Helvetica",40,"bold"),background="light green")
        label_top.pack(side=tk.LEFT, padx=5, pady=5,fill=tk.X,expand=1)

        icon_frame = tk.Frame(top_frame, bg="lightgray")
        icon_frame.pack(side=tk.RIGHT)
        image=tk.Label(icon_frame, image=self.icon)
        image.pack(side=tk.TOP, fill=tk.BOTH)

        button_top = tk.Button(top_frame, text="Change Password",height=5,command=lambda:change_password(self.user))
        button_top.pack(side=tk.RIGHT)

        # Bottom frame (80% of the space)
        bottom_frame = tk.Frame(self)
        bottom_frame.grid(row=1, column=0, sticky="nsew")

        label_start = tk.Label(bottom_frame, text="Starting Funds: "+str(self.user.get_starting_funds()))
        label_start.configure(font=("Arial",18))
        label_start.grid(row=0, column=0, sticky="w")

        label_curr = tk.Label(bottom_frame, text="Current Funds: "+str(self.user.get_current_funds()))
        label_curr.configure(font=("Arial", 18))
        label_curr.grid(row=2, column=0, sticky="w")

        label_prof = tk.Label(bottom_frame, text="Current profit: " + str(self.user.get_profit_percent()))
        label_prof.configure(font=("Arial", 18))
        label_prof.grid(row=3, column=0, sticky="w")

        label_perc = tk.Label(bottom_frame, text="Current profit percentage: "+str(self.user.get_profit_percent()))
        label_perc.configure(font=("Arial", 18))
        label_perc.grid(row=4, column=0, sticky="w")
