import customtkinter as ctk

class ErrorPopup(ctk.CTk):
    '''simple error popup'''
    def __init__(self,message:str):
        super().__init__()
        self.title = "Error"
        ctk.CTkLabel(self, text=message).pack()
        ctk.CTkButton(self, text="OK", command=lambda: self.destroy()).pack()
        self.mainloop()
