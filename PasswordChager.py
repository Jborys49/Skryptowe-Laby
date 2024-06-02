import time
import tkinter as tk
import yfinance as yf
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from User import User
from Transaction import Transaction
from decimal import Decimal
import Event
import os

def changePassword(password1: str, password2: str,user: User,master:tk.Tk) -> None:
    if password1 == password2:
        user.set_password(password1)
        master.destroy()
    else:
        error = tk.Tk()
        error.minsize(200, 100)
        tk.Label(error, text="Password must match").pack()
        tk.Button(error, text="OK", command=lambda: error.destroy()).pack()

class PasswordChager(tk.Tk):
    def __init__(self,user):
        super().__init__()
        self.user = user
        self.title("Password Chager")
        self.minsize(width=100,height=100)
        self.resizable(False, False)
        main_frame = tk.Frame(self)
        main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        password1 = tk.Label(main_frame, text="Input your password:")
        password1.grid(row=0, column=0)
        password2 = tk.Label(main_frame, text="Input your password again:")
        password2.grid(row=1, column=0)
        passentry1 = tk.Entry(main_frame)
        passentry1.grid(row=0, column=1)
        passentry2 = tk.Entry(main_frame)
        passentry2.grid(row=1, column=1)
        execute=tk.Button(main_frame, text="Change",command=lambda: changePassword(passentry1.get(),passentry2.get(),self.user,self))
        execute.grid(row=2,column=0,rowspan=2,columnspan=1)
