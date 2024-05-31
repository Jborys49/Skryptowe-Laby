import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from User import User
from Buy_Screen import BuyScreen
import Event
import os


def clear_main_frame(frame: tk.Frame):
    print('works')
    for widget in frame.winfo_children():
        widget.destroy()
    Label(frame, text="Click one of the buttons for functionality", font=("Arial", 32)).pack(fill=tk.BOTH,
                                                                                             expand=1)


def execute_buying(frame: tk.Frame, user: User):
    for widget in frame.winfo_children():
        widget.destroy()
    BuyScreen(frame,user).pack(side=tk.TOP, fill=tk.BOTH, expand=True)


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

        profile_button = tk.Button(top_frame, text="Profile")
        profile_button.pack(side=tk.LEFT, expand=True)

        # Create the bottom frame to fill the rest of the interface
        bottom_frame = tk.Frame(self, bg="white")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True,padx=10,pady=10)

        day_button = tk.Button(top_frame, text="Next Day",command=clear_main_frame(bottom_frame))
        day_button.pack(side=tk.LEFT, expand=True)
        # Create Buy, Sell, and Profile buttons with equal spacing
        buy_button = tk.Button(top_frame, text="Buy",command=lambda:execute_buying(bottom_frame, self.user))
        buy_button.pack(side=tk.LEFT, expand=True)

        sell_button = tk.Button(top_frame, text="Sell")
        sell_button.pack(side=tk.LEFT, expand=True)


if __name__ == "__main__":
    app = Interface(user=User('bingo','bango',200.0))
    app.mainloop()
    print("wtf")