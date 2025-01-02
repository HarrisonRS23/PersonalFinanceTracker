from tkinter import *
import customtkinter as ctk

import plaid
from plaid.api import plaid_api

# Window Setup 

ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry('300x400')
root.title("Personal Finance Tracker")
button = ctk.CTkButton(master=root,text="Hello world")

button.place(relx=0.5,rely=0.5, anchor = CENTER )

root.mainloop()


