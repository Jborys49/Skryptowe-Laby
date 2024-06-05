import datetime
import customtkinter as ctk
from decimal import Decimal
from PIL import ImageTk, Image

from User import User
from Transaction import Transaction
import Event

class Wallet(ctk.CTkFrame):
    '''The Wallet class displays all stocks owneb by the users and allows him to sell them'''
    def __init__(self, parent,user:User):
        super().__init__(parent)
        self.user = user
        self.parent = parent

        self.pack(fill=ctk.BOTH, expand=1)
        self.canvas = ctk.CTkCanvas(self,background="dark grey")
        self.scrollbar = ctk.CTkScrollbar(self, command=self.canvas.yview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_frame.pack(fill=ctk.BOTH,expand=True)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)
        self.scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

        self.wallet=self.user.get_wallet()
        for entry in self.wallet:
            frame = ctk.CTkFrame(self.scrollable_frame)
            label = ctk.CTkLabel(frame, text='Stock:'+entry+" with shares: "+ str(self.wallet[entry]["shares"])+
                             " Paid for stocks: "+ str(self.wallet[entry]["paid"]))
            #button1 = ctk.CTkButton(frame, text="View stock trend",command=lambda:stock_trend(entry,self.user.get_date()) )
            button2 = ctk.CTkButton(frame, text="Sell",command=lambda:self.sell_stock(frame,label,self.user,entry,
                                                                             Event.get_price(entry,self.user.get_date(),1)))

            label.pack(side="left",fill=ctk.X, padx=5)
            #button1.pack(side="right", padx=5)
            button2.pack(side="right", padx=5)

            frame.pack(fill="x", pady=5)

    def sell_stock(sefl,frame, label, user: User, stock: str, price: Decimal):
        '''Invokes transaction to sell some amount of stock'''
        seller = Transaction(user, stock, price, 1, frame, label)
        seller.mainloop()
