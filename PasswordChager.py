import tkinter as tk
import customtkinter as ctk
from User import User
import Event

def changePassword(password1: str, password2: str,user: User,master:tk.Tk) -> None:
    if password1 == password2:
        user.set_password(password1)
        Event.save_user(user)
        master.destroy()
    else:
        error = ctk.CTk()
        error.minsize(200, 100)
        ctk.CTkLabel(error, text="Password must match").pack()
        ctk.CTkButton(error, text="OK", command=lambda: error.destroy()).pack()

class PasswordChager(ctk.CTk):
    def __init__(self,user):
        super().__init__()
        self.user = user
        self.title("Password Chager")
        self.minsize(width=100,height=100)
        self.resizable(False, False)
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)
        password1 = ctk.CTkLabel(main_frame, text="Input your password:")
        password1.grid(row=0, column=0)
        password2 = ctk.CTkLabel(main_frame, text="Input your password again:")
        password2.grid(row=1, column=0)
        passentry1 = ctk.CTkEntry(main_frame,show="*")
        passentry1.grid(row=0, column=1)
        passentry2 = ctk.CTkEntry(main_frame,show="*")
        passentry2.grid(row=1, column=1)
        execute=ctk.CTkButton(main_frame, text="Change",command=lambda: changePassword(passentry1.get(),passentry2.get(),self.user,self))
        execute.grid(row=2,column=0,rowspan=2,columnspan=1)
