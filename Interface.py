import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from User import User
import Event
import os

class Interface:
    def __init__(self,user:User):
        self.user = user
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", Event.end_session(self.user))