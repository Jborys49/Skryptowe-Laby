import customtkinter as ctk
import yfinance as yf
from PIL import ImageTk, Image

from User import User
from Transaction import Transaction
from decimal import Decimal
import Event

def get_name(stock:str)->str:
    '''Some stocks do not have Long or Short names so we use the best ones availible'''
    try:
        return yf.Ticker(stock).info['longName']
    except:
        try:
            return yf.Ticker(stock).info['shortName']
        except:
            return stock
def embed_graph(frame:ctk.CTkFrame,image:ImageTk.PhotoImage):
    '''put graph in StockDetailsFrame'''
    for widget in frame.winfo_children():
        widget.destroy()
    imglbl=ctk.CTkLabel(frame,image=image)
    imglbl.image=image
    imglbl.pack()
def buy_stock(user:User,stock:str,price:Decimal):
    '''InvokeTransaction to buy shares of stock'''
    seller=Transaction(user,stock,price,0)
    seller.mainloop()
class StockDetails(ctk.CTkFrame):
    '''Class has the graphs for stock trends and the buy button'''
    def __init__(self, parent:ctk.CTkFrame,user:User,stock:str):
        super().__init__(parent)
        self.user=user
        self.stock=stock

        self.stock_records,self.volume=Event.fetch_and_save_stock_data(stock,user.get_date())

        #We have to do this because python garbage collector will delete images with no solid reference
        Event.plot_stock(self.stock, self.stock_records)
        self.weekplot=ImageTk.PhotoImage(Image.open('Stock_Graphs/'+self.stock+"1w.png"))
        self.monthplot=ImageTk.PhotoImage(Image.open('Stock_Graphs/'+self.stock + "1m.png"))
        self.month2plot=ImageTk.PhotoImage(Image.open('Stock_Graphs/'+self.stock + "2m.png"))

        main_frame = ctk.CTkFrame(self)
        main_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

        # Configure the grid layout
        main_frame.columnconfigure(0, weight=9)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

        # Create the left frame
        left_frame = ctk.CTkFrame(main_frame)
        left_frame.grid(row=0, column=0)

        # Create the right frame
        right_frame = ctk.CTkFrame(main_frame)
        right_frame.grid(row=0, column=1, sticky="nsew")

        # Add text components and buttons to the left frame
        text1 = ctk.CTkLabel(right_frame, text=get_name(self.stock),font=("Helvetica",14))
        text1.pack(pady=10,fill=ctk.BOTH, expand=True)

        text2 = ctk.CTkLabel(right_frame,text='Volume: '+str(self.volume))
        text2.pack(pady=10,fill=ctk.BOTH, expand=True)

        button1 = ctk.CTkButton(right_frame, text="1 Week",command=lambda:embed_graph(left_frame,self.weekplot))
        button1.pack(pady=5,fill=ctk.BOTH, expand=True)

        button2 = ctk.CTkButton(right_frame, text="1 Month",command=lambda:embed_graph(left_frame,self.monthplot))
        button2.pack(pady=5,fill=ctk.BOTH, expand=True)

        button3 = ctk.CTkButton(right_frame, text="2 Months",command=lambda:embed_graph(left_frame,self.month2plot))
        button3.pack(pady=5,fill=ctk.BOTH, expand=True)

        button4 = ctk.CTkButton(right_frame, text="BUY",command=lambda:buy_stock(self.user,self.stock,Event.get_price(self.stock,self.user.get_date(),0)))
        button4.pack(pady=5,fill=ctk.BOTH, expand=True)

