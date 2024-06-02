import tkinter as tk
from Login import Login
import os


class StockTradingInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stock Simulator")
        self.minsize(800, 500)
        log = Login(self)
        log.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.mainloop()
        self.protocol("WM_DELETE_WINDOW", self.quit)

    def quit(self):
        self.clean_pdf()
        self.destroy()
    def clean_pdf(self):
        for file in os.listdir('Stock_Graphs'):
            os.unlink(os.path.join('Stock_Graphs', file))
pmi=StockTradingInterface()