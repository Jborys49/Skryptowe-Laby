import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from User import User
import Event
import os

class Interface(tk.Tk):
    def __init__(self,user:User):
        super().__init__()
        self.user = user
        # Set the minimum size of the window
        # Set the minimum size of the window
        self.minsize(800, 500)
        self.title("Interface")
        self.configure(bg="light blue")

        # Create the top frame for Buy, Sell, and Profile buttons
        top_frame = tk.Frame(self, bg="lightgray",height=70)
        top_frame.pack_propagate(0)
        top_frame.pack(side=tk.TOP,fill=tk.X,padx=10,pady=10)

        # Create Buy, Sell, and Profile buttons with equal spacing
        buy_button = tk.Button(top_frame, text="Buy")
        buy_button.pack(side=tk.LEFT, expand=True)

        sell_button = tk.Button(top_frame, text="Sell")
        sell_button.pack(side=tk.LEFT, expand=True)

        profile_button = tk.Button(top_frame, text="Profile")
        profile_button.pack(side=tk.LEFT, expand=True)

        day_button = tk.Button(top_frame, text="Next Day",command=self.clear_main_frame())
        day_button.pack(side=tk.LEFT, expand=True)

        # Create the bottom frame to fill the rest of the interface
        bottom_frame = tk.Frame(self, bg="white")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True,padx=10,pady=10)
    def clear_main_frame(self):
        for widget in self.winfo_children():
            print(widget)
            #widget.destroy()
        #Label(self.bottom_frame,text="Click one of the buttons for functionality")
if __name__ == "__main__":
    app = Interface(user=User('bingo','bango',200.0))
    app.mainloop()
    print("wtf")