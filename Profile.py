import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image

from User import User
from PasswordChager import PasswordChager


class Profile(ctk.CTkFrame):
    '''Displays user stats, allows him to change his password'''
    def __init__(self,parent,user:User):
        super().__init__(parent)
        self.user=user
        self.icon=ImageTk.PhotoImage(Image.open('Program_Icons/userPic.png').resize((100,100)))

        # Configure grid layout for the main frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)  # Give more weight to bottom frame
        self.grid_columnconfigure(0, weight=1)

        # Top frame (20% of the space)
        top_frame = ctk.CTkFrame(self)
        top_frame.configure(fg_color=("dark yellow","dark green"))
        top_frame.grid(row=0, column=0, sticky="nsew")

        label_top = ctk.CTkLabel(top_frame, text=user.get_login())
        label_top.configure(font=("Helvetica",40,"bold"))
        label_top.pack(side=ctk.LEFT, padx=5, pady=5,fill=ctk.X,expand=1)

        icon_frame = ctk.CTkFrame(top_frame)
        icon_frame.pack(side=ctk.RIGHT)
        image=ctk.CTkLabel(icon_frame, image=self.icon,text="")
        image.pack(side=ctk.TOP, fill=ctk.BOTH)

        button_top = ctk.CTkButton(top_frame, text="Change Password",command=lambda:self.change_password(self.user))
        button_top.pack(side=ctk.RIGHT)

        # Bottom frame (80% of the space)
        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.grid(row=1, column=0, sticky="nsew")

        label_start = ctk.CTkLabel(bottom_frame, text="Starting Funds: "+str(self.user.get_starting_funds()))
        label_start.configure(font=("Arial",18))
        label_start.pack(side=ctk.TOP, fill=ctk.X,expand=True)

        label_curr = ctk.CTkLabel(bottom_frame, text="Current Funds: "+str(self.user.get_current_funds()))
        label_curr.configure(font=("Arial", 18))
        label_curr.pack(side=ctk.TOP, fill=ctk.X,expand=True)

        label_prof = ctk.CTkLabel(bottom_frame, text="Current profit: " + str(self.user.get_current_funds()-self.user.get_starting_funds()))
        label_prof.configure(font=("Arial", 18))
        label_prof.pack(side=ctk.TOP, fill=ctk.X,expand=True)

        label_perc = ctk.CTkLabel(bottom_frame, text="Current profit percentage: "+str(self.user.get_profit_percent()))
        label_perc.configure(font=("Arial", 18))
        label_perc.pack(side=ctk.TOP, fill=ctk.X,expand=True)

        canvas = ctk.CTkCanvas(bottom_frame, background="dark grey")
        scrollbar = ctk.CTkScrollbar(bottom_frame, command=canvas.yview)
        scrollable_frame = ctk.CTkFrame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        scrollable_frame.pack(fill=ctk.BOTH, expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)
        scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

        history = self.user.get_history()
        for entry in history:
            frame = ctk.CTkFrame(scrollable_frame)
            label = ctk.CTkLabel(frame, text=self.display_history_entry(entry))

            label.pack(side="left", fill=ctk.X, padx=5)

            frame.pack(fill="x", pady=5)

    def display_history_entry(self,entry: dict):
        if entry['is_purchase'] == True:
            return "On " + entry['date'].strftime("%Y/%m/%d") + " purchased " + str(entry['shares']) + " " + entry[
                'name'] + " stocks at price " + str(entry['price'])
        else:
            return "On " + entry['date'].strftime("%Y/%m/%d") + " sold " + str(entry['shares']) + " " + entry[
                'name'] + " stocks at price " + str(entry['price'])

    def change_password(self,user: User):
        '''invokes PasswordChanger for user'''
        pswd = PasswordChager(user)
        pswd.mainloop()