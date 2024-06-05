from datetime import datetime
import customtkinter as ctk
import tkinter as tk
from decimal import Decimal
import pickle

from ErrorPopup import ErrorPopup
from Interface import Interface
from User import User
import Event
import os

folder_path='Stock_Users'





class Login(ctk.CTkFrame):
    '''Class handles loging in users and registering new ones. can invoke ErrorPopups when the user tries to do illegal actions'''
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent

        self.pack(side=tk.TOP,fill=tk.BOTH,expand=1)

        login_text=ctk.CTkLabel(self,text="Login",font=("Roboto",24))
        login_text.pack(side=ctk.TOP,fill=tk.X,expand=True)
        login_entry=ctk.CTkEntry(self,placeholder_text="Username")
        login_entry.pack(side=ctk.TOP,expand=True)
        password_entry=ctk.CTkEntry(self,placeholder_text="Password",show="*")
        password_entry.pack(side=ctk.TOP,expand=True)
        btn_login=ctk.CTkButton(self,text="Login",command=lambda:self.login_user(login_entry.get(),password_entry.get(),self.parent))
        btn_login.pack(side=ctk.TOP)

        register_text = ctk.CTkLabel(self, text="Register", font=("Roboto", 24))
        register_text.pack(side=ctk.TOP,  expand=True)
        register_login = ctk.CTkEntry(self, placeholder_text="Username")
        register_login.pack(side=ctk.TOP,  expand=True)
        register_password = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        register_password.pack(side=ctk.TOP, expand=True)
        register_bud = ctk.CTkEntry(self, placeholder_text="Budget")
        register_bud.pack(side=ctk.TOP, expand=True)
        register_year = ctk.CTkEntry(self, placeholder_text="Year")
        register_year.pack(side=ctk.TOP,  expand=True)
        register_month = ctk.CTkEntry(self, placeholder_text="Month")
        register_month.pack(side=ctk.TOP,  expand=True)
        register_day = ctk.CTkEntry(self, placeholder_text="Day")
        register_day.pack(side=ctk.TOP,  expand=True)
        btn_register = ctk.CTkButton(self, text="Register",
                                  command=lambda: self.register_user(register_login.get(), register_password.get(),
                                                                register_bud.get(),register_year.get()+"-"+register_month.get()+"-"+register_day.get(),self.parent))
        btn_register.pack(side=ctk.TOP)

    def check_for_user(self,login: str) -> bool:
        '''This method checks if we have saved an user in the database'''
        return os.path.isfile(folder_path + "\\" + login)

    def check_password(self,login: str, password: str) -> User:
        '''method checks whether an *existing* user has the same password as provided'''
        # we have to open the file in binary mode for pickle
        user_file = open(folder_path + "\\" + login, "rb")
        currentUser = pickle.load(user_file)
        return password == currentUser.get_password()
    def login_user(self,login:str,password:str,parent:tk.Tk):
        '''method returns user if user exists and password matches,else throws error'''
        if self.check_for_user(login):
            if self.check_password(login,password):
                user_file = open(folder_path + "\\" + login,"rb")
                currentUser = pickle.load(user_file)
                for widget in parent.winfo_children():
                    widget.destroy()
                inter=Interface(parent,currentUser)
                inter.pack(side=ctk.TOP,fill=ctk.BOTH,expand=True)
            else:
                error=ErrorPopup("Incorrect password")
        else:
            error=ErrorPopup("User not Registered")

    def register_user(self,login:str,password:str,starting_funds:str,date:str,parent:tk.Tk):
        '''registers a new user in the database if the login isnt already taken'''
        if self.check_for_user(login):
            error = ErrorPopup("Username already in Use")
        else:
            try:
                stock_date = datetime.strptime(date,'%Y-%m-%d').date()
                if stock_date < datetime(2005,1,1).date() or stock_date > datetime(2010,1,1).date():
                    error=ErrorPopup("Date not in specified range of 2005 to 2009")
            except:
                error=ErrorPopup("Date format does not match")
            else:
                try:
                    starting_funds = float(starting_funds)
                except:
                    error=ErrorPopup("Funds format does not match")
                else:
                    currentUser = User(login, password, Decimal(starting_funds).quantize(Decimal('1.00')), stock_date)
                    Event.save_user(currentUser)
                    self.login_user(login, password, parent)