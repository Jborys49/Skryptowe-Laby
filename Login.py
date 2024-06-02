import datetime
import tkinter as tk
from decimal import Decimal
import pickle
from Interface import Interface
from User import User
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


def login(login:str,password:str):
    global currentUser
    '''method returns user if user exists and password matches,else throws error'''
    if check_for_user(login):
        if check_password(login,password):
            user_file = open(folder_path + "\\" + login,"rb")
            currentUser = pickle.load(user_file)
            inter=Interface(currentUser)
            inter.mainloop()
        else:
            raise Exception("Wrong password")
    else:
        raise Exception("User not registered in system")

def register_user(login:str,password:str,starting_funds:float,date:str)->User:
    '''registers a new user in the database if the login isnt already taken'''
    if check_for_user(login):
        raise Exception("Login already taken")
    stock_date = date.strftime('%Y-%m-%d')
    currentUser=User(login,password,Decimal(starting_funds).quantize(Decimal('1.00')),stock_date)
    return currentUser


def end_session(currentUser:User)->bool:
    '''method saves the user to teh databes- used in relogging and closing the program'''
    dest_path=folder_path+"\\"+currentUser.get_login()
    if os.path.exists(dest_path):
        os.remove(dest_path)
    file=open(dest_path, "ab")
    pickle.dump(currentUser,file)
    file.close()
    return True


class Login(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        LoginScreen=tk.Frame(self)
        LoginScreen.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        #LoginScreen.title("Zaloguj się lub zarejestruj")
        LoginScreen.configure(background="dark gray")
        #LoginScreen.minsize(800,500)
        tk.Label(LoginScreen,text="Login").grid(row=0)
        tk.Label(LoginScreen,text="Password").grid(row=1)
        #if i define the grid in the same row as the entry its not a entry but a none
        LoginVal=tk.Entry(LoginScreen)
        LoginVal.grid(row=0,column=1)
        PasswordVal=tk.Entry(LoginScreen)
        PasswordVal.grid(row=1,column=1)
        LoginButton=tk.Button(LoginScreen,text="Zaloguj się",command=lambda:login(LoginVal.get(),PasswordVal.get()))
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
        RegisterButton=tk.Button(LoginScreen,text="Zarejestruj się",command=lambda:register_user(RegisterLogin.get(),RegisterPassword.get(),RegisterDate.get()))
        RegisterButton.grid(row=8)
        LoginScreen.mainloop()
