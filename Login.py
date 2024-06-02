from datetime import datetime
import tkinter as tk
from decimal import Decimal
import pickle
from Interface import Interface
from User import User
import Event
import os

folder_path='Stock_Users'

def check_for_user(login:str)->bool:
    '''This method checks if we have saved an user in the database'''
    return os.path.isfile(folder_path+"\\"+login)

def check_password(login:str,password:str)->User:
    '''method checks whether an *existing* user has the same password as provided'''
    #we have to open the file in binary mode for pickle
    user_file=open(folder_path+"\\"+login, "rb")
    currentUser=pickle.load(user_file)
    return password==currentUser.get_password()


def login_user(login:str,password:str,parent:tk.Tk):
    '''method returns user if user exists and password matches,else throws error'''
    if check_for_user(login):
        if check_password(login,password):
            user_file = open(folder_path + "\\" + login,"rb")
            currentUser = pickle.load(user_file)
            for widget in parent.winfo_children():
                widget.destroy()
            print(currentUser.get_date())
            inter=Interface(parent,currentUser)
            inter.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        else:
            raise Exception("Wrong password")
    else:
        raise Exception("User not registered in system")

def register_user(login:str,password:str,starting_funds:float,date:str,parent:tk.Tk):
    '''registers a new user in the database if the login isnt already taken'''
    if check_for_user(login):
        error = tk.Tk()
        error.minsize(200, 100)
        tk.Label(error, text="Username already in use").pack()
        tk.Button(error, text="OK", command=lambda: error.destroy()).pack()
    else:
        stock_date = datetime.strptime(date,'%Y-%m-%d').date()
        currentUser=User(login,password,Decimal(starting_funds).quantize(Decimal('1.00')),stock_date)
        Event.save_user(currentUser)
        login_user(login,password,parent)




class Login(tk.Frame):
    def __init__(self,parent):
        print('Works')
        super().__init__(parent)
        self.parent=parent

        self.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        LoginScreen=tk.Frame(self)
        LoginScreen.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        LoginScreen.configure(background="dark gray")

        tk.Label(LoginScreen,text="Login").grid(row=0)
        tk.Label(LoginScreen,text="Password").grid(row=1)
        LoginVal=tk.Entry(LoginScreen)
        LoginVal.grid(row=0,column=1)
        PasswordVal=tk.Entry(LoginScreen)
        PasswordVal.grid(row=1,column=1)
        LoginButton=tk.Button(LoginScreen,text="Log in",command=lambda:login_user(LoginVal.get(),PasswordVal.get(),self.parent))
        LoginButton.grid(row=3)

        RegisterLogin=tk.Entry(LoginScreen)
        RegisterPassword=tk.Entry(LoginScreen)
        RegisterBudget=tk.Entry(LoginScreen)
        RegisterDate=tk.Entry(LoginScreen)
        tk.Label(LoginScreen,text="Register Login").grid(row=4)
        RegisterLogin.grid(row=4,column=1)
        tk.Label(LoginScreen,text="Register Password").grid(row=5)
        RegisterPassword.grid(row=5,column=1)
        tk.Label(LoginScreen,text="Register Budget").grid(row=6)
        RegisterBudget.grid(row=6,column=1)
        tk.Label(LoginScreen,text="Register Date").grid(row=7)
        RegisterDate.grid(row=7,column=1)
        RegisterButton=tk.Button(LoginScreen,text="Register",command=lambda:register_user(RegisterLogin.get(),RegisterPassword.get(),float(RegisterBudget.get()),RegisterDate.get(),self.parent))
        RegisterButton.grid(row=8)
