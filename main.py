from tkinter import *
import customtkinter as ctk

import plaid
from plaid.api import plaid_api


ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
  def __init__(self):
    super().__init__()

    # Window Setup 
    self.title("Harrison Finance Tracker")
    self.geometry("1100x580")

    # Configure grid layout (4x4) (non-zero weight will expand proportionally to weight value)
    self.grid_columnconfigure(1, weight=1) # Column 1 has a weight of 1
    self.grid_columnconfigure((2, 3), weight=0) # Column 2 and 3 weight 0 (will not expand)
    self.grid_rowconfigure((0, 1, 2), weight=1) # Row 0, 1, 2 weight of 1

    # Create a sidebar fram with widgets

    self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
    # Spans 4 rows in column 1, "nsew": Stretch in all directions to fill the entire cell.
    self.sidebar_frame.grid(row=0,column=0,rowspan=4,sticky="nsew")
    self.sidebar_frame.grid_rowconfigure(4, weight=1)
    # Add text at top of sidebar
    self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Placeholder", font=ctk.CTkFont(size=20, weight="bold"))
    self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))


if __name__ == "__main__":
    app = App()
    app.mainloop()



