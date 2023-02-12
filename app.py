import customtkinter
from tkinter import *
from tkinter import messagebox
import os


os.system('clear')
app_width = 500
app_height = 500

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{app_width}x{app_height}')
        self.title('World')


        lab = customtkinter.CTkLabel(self, text="HELLO WORLD").pack()


app = App()
app.mainloop()