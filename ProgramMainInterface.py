import tkinter as tk
import customtkinter as ctk
from Login import Login
import Event
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
class StockTradingInterface(ctk.CTk):
    '''the class holding the overall gui'''
    def __init__(self):
        super().__init__()
        self.title("Stock Simulator")
        self.minsize(800, 500)
        log = Login(self)
        log.pack(side=ctk.TOP, fill=ctk.BOTH, expand=1)
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.mainloop()

    def quit(self):
        Event.clean_pdf()
        self.destroy()
