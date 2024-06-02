import tkinter as tk
import os

from User import User
from Buy_Screen import BuyScreen
from Wallet import Wallet
from Profile import Profile
import Event


def next_day(frame: tk.Frame,user:User,label:tk.Label):
    for widget in frame.winfo_children():
        widget.destroy()
    for file in os.listdir('Stock_Graphs'):
        os.unlink(os.path.join('Stock_Graphs', file))
    user.next_day()
    Event.save_user(user)
    label.config(text=user.get_date().strftime("%Y-%d-%m"))
    tk.Label(frame, text="Click one of the buttons for functionality", font=("Arial", 32)).pack(fill=tk.BOTH,expand=1)
def clear_bottom(frame: tk.Frame):
    for widget in frame.winfo_children():
        widget.destroy()
    tk.Label(frame, text="Click one of the buttons for functionality", font=("Arial", 32)).pack(fill=tk.BOTH, expand=1)
def execute_buying(frame: tk.Frame, user: User):
    for widget in frame.winfo_children():
        widget.destroy()
    BuyScreen(frame,user).pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def execute_selling(frame: tk.Frame, user: User):
    for widget in frame.winfo_children():
        widget.destroy()
    Wallet(frame,user).pack(side=tk.TOP, fill=tk.BOTH,expand=True)
def execute_profile(frame:tk.Frame, user: User):
    for widget in frame.winfo_children():
        widget.destroy()
    Profile(frame,user).pack(side=tk.TOP, fill=tk.BOTH,expand=True)
class Interface(tk.Frame):

    def __init__(self,parent,user:User):
        super().__init__(parent)
        self.user = user
        self.configure(bg="light blue")
        self.pack(side=tk.TOP,fill=tk.BOTH, expand=1)
        # Create the top frame for Buy, Sell, and Profile buttons
        top_frame = tk.Frame(self, bg="lightgray",height=70)
        top_frame.pack_propagate(False)
        top_frame.pack(side=tk.TOP,fill=tk.X,padx=10,pady=10)

        # Create the bottom frame to fill the rest of the interface
        bottom_frame = tk.Frame(self, bg="white")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)

        profile_button = tk.Button(top_frame, text="Profile",command=lambda:execute_profile(bottom_frame, self.user))
        profile_button.pack(side=tk.LEFT, expand=True)


        day_button = tk.Button(top_frame, text="Next Day",command=lambda:next_day(bottom_frame,self.user,date_label))
        day_button.pack(side=tk.LEFT, expand=True)
        # Create Buy, Sell, and Profile buttons with equal spacing
        buy_button = tk.Button(top_frame, text="Buy",command=lambda:execute_buying(bottom_frame, self.user))
        buy_button.pack(side=tk.LEFT, expand=True)

        sell_button = tk.Button(top_frame, text="Sell",command=lambda:execute_selling(bottom_frame, self.user))
        sell_button.pack(side=tk.LEFT, expand=True)

        date_label=tk.Label(top_frame, text=self.user.get_date().strftime("%Y-%d-%m"))
        date_label.pack(side=tk.LEFT,expand=True)
        clear_bottom(bottom_frame)
