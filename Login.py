import datetime
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from decimal import Decimal
import pickle
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


def return_user(login:str,password:str)->User:
    global currentUser
    '''method returns user if user exists and password matches,else throws error'''
    if check_for_user(login):
        if check_password(login,password):
            user_file = open(folder_path + "\\" + login,"rb")
            currentUser = pickle.load(user_file)
            return currentUser
        else:
            raise Exception("Wrong password")
    else:
        raise Exception("User not registered in system")
def register_user(login:str,password:str,starting_funds:float,date:str)->User:
    '''registers a new user in the database if the login isnt already taken'''
    if check_for_user(login):
        raise Exception("Login already taken")
    stock_date = date.strftime('%Y-%m-%d')
    currentUser=User(login,password,starting_funds,stock_date)
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

def login(currentUser:User)->bool:
    return True
#newUser=register_user("bingo","bango",200.0)
#end_session(register_user("bingo","bango",200.0))

LoginScreen=Tk()
LoginScreen.title("Zaloguj się lub zarejestruj")
LoginScreen.configure(background="dark gray")
LoginScreen.minsize(800,500)
Label(LoginScreen,text="Login").grid(row=0)
Label(LoginScreen,text="Password").grid(row=1)
#if i define the grid in the same row as the entry its not a entry but a none
LoginVal=tkinter.Entry(LoginScreen)
LoginVal.grid(row=0,column=1)
PasswordVal=tkinter.Entry(LoginScreen)
PasswordVal.grid(row=1,column=1)
LoginButton=Button(LoginScreen,text="Zaloguj się",command=lambda:return_user(LoginVal.get(),PasswordVal.get()))
LoginButton.grid(row=3)

RegisterLogin=tkinter.Entry(LoginScreen)
RegisterPassword=tkinter.Entry(LoginScreen)
RegisterBudget=tkinter.Entry(LoginScreen)
RegisterDate=tkinter.Entry(LoginScreen)
Label(LoginScreen,text="Register Login").grid(row=4)
RegisterLogin.grid(row=4,column=1)
Label(LoginScreen,text="Register Password").grid(row=5)
RegisterPassword.grid(row=5,column=1)
Label(LoginScreen,text="Register Budget").grid(row=6)
RegisterBudget.grid(row=6,column=1)
Label(LoginScreen,text="Register Date").grid(row=7)
RegisterDate.grid(row=7,column=1)
RegisterButton=Button(LoginScreen,text="Zarejestruj się",command=lambda:register_user(RegisterLogin.get(),RegisterPassword.get(),RegisterDate.get()))
RegisterButton.grid(row=8)
LoginScreen.mainloop()
#newUser=return_user("bingo","bango")
#newUser.print()
#end_session(newUser)