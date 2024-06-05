import customtkinter as ctk
import os

from User import User
from Buy_Screen import BuyScreen
from Wallet import Wallet
from Profile import Profile
import Event



class Interface(ctk.CTkFrame):
    '''Main class of the program, lets the user go to different functionalities of the program'''
    def __init__(self,parent,user:User):
        super().__init__(parent)
        self.user = user
        self.parent = parent
        #self.configure(bg="light blue")
        self.pack(side=ctk.TOP,fill=ctk.BOTH, expand=1)
        # Create the top frame for Buy, Sell, and Profile buttons
        top_frame = ctk.CTkFrame(self,height=70)
        top_frame.pack_propagate(False)
        top_frame.pack(side=ctk.TOP,fill=ctk.X,padx=10,pady=10)

        # Create the bottom frame to fill the rest of the interface
        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.pack(side=ctk.BOTTOM, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        profile_button = ctk.CTkButton(top_frame, text="Profile",command=lambda:self.execute_profile(bottom_frame, self.user))
        profile_button.pack(side=ctk.LEFT, expand=True)


        day_button = ctk.CTkButton(top_frame, text="Next Day",command=lambda:self.next_day(bottom_frame,self.user,date_label))
        day_button.pack(side=ctk.LEFT, expand=True)
        # Create Buy, Sell, and Profile buttons with equal spacing
        buy_button = ctk.CTkButton(top_frame, text="Buy",command=lambda:self.execute_buying(bottom_frame, self.user))
        buy_button.pack(side=ctk.LEFT, expand=True)

        sell_button = ctk.CTkButton(top_frame, text="Sell",command=lambda:self.execute_selling(bottom_frame, self.user))
        sell_button.pack(side=ctk.LEFT, expand=True)

        sell_button = ctk.CTkButton(top_frame, text="Logout", command=lambda: self.logout(self.parent, self.user))
        sell_button.pack(side=ctk.BOTTOM, expand=True)

        date_label=ctk.CTkLabel(top_frame, text="Current Date: "+self.user.get_date().strftime("%Y-%m-%d"))
        date_label.pack(side=ctk.LEFT,expand=True)
        self.clear_bottom(bottom_frame)

    def next_day(self,frame: ctk.CTkFrame, user: User, label: ctk.CTkLabel):
        '''Advance the user by a day, which will change their price'''
        for widget in frame.winfo_children():
            widget.destroy()
        for file in os.listdir('Stock_Graphs'):
            os.unlink(os.path.join('Stock_Graphs', file))
        user.next_day()
        Event.save_user(user)
        label.configure(text='Current Date: ' + user.get_date().strftime("%Y-%m-%d"))
        ctk.CTkLabel(frame, text="Click one of the buttons for functionality", font=("Arial", 32)).pack(fill=ctk.BOTH,
                                                                                                        expand=1)

    def clear_bottom(self,frame: ctk.CTkFrame):
        '''Clear bottom frame for readability'''
        for widget in frame.winfo_children():
            widget.destroy()
        ctk.CTkLabel(frame, text="Click one of the buttons for functionality", font=("Arial", 32)).pack(fill=ctk.BOTH,
                                                                                                        expand=1)

    def execute_buying(self,frame: ctk.CTkFrame, user: User):
        '''Invoke BuyScreen for buying stock by user'''
        for widget in frame.winfo_children():
            widget.destroy()
        BuyScreen(frame, user).pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

    def execute_selling(self,frame: ctk.CTkFrame, user: User):
        '''Execute selling for selling stock by user'''
        for widget in frame.winfo_children():
            widget.destroy()
        Wallet(frame, user).pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

    def execute_profile(self,frame: ctk.CTkFrame, user: User):
        '''Invoke Profile screen for stats'''
        for widget in frame.winfo_children():
            widget.destroy()
        Profile(frame, user).pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

    def logout(self,frame: ctk.CTkFrame, user: User):
        '''Saves user information to file and goes back to Login'''
        from Login import Login
        for widget in frame.winfo_children():
            widget.destroy()
        Event.save_user(user)
        Event.clean_pdf()
        Login(frame)