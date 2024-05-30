import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from User import User
import os

class Interface:
    def __init__(self,user:User):
        self.user = user