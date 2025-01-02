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


    # Create a sidebar frame with widgets
    def create_side_bar(self):
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        # Spans 4 rows in column 1, "nsew": Stretch in all directions to fill the entire cell.
        self.sidebar_frame.grid(row=0,column=0,rowspan=4,sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # Add text at top of sidebar
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Placeholder", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Add sidebar buttons 
        self.sidebar_home_button = ctk.CTkButton(self.sidebar_frame,text = "Home", command=self.sidebar_button_event)
        self.sidebar_home_button.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_expenses_button =  ctk.CTkButton(self.sidebar_frame,text="Expenses", command=self.sidebar_button_event)
        self.sidebar_expenses_button.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        # Add appearance settings
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


    def create_home_screen(self):
        print("Creating homescreen")

        # Clear Screen 
        for widget in self.winfo_children():
            widget.destroy()  # Clear the current screen

        self.create_side_bar()

    def open_input_dialog_event(self):
        dialog = ctk.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    # Change between light, dark, and system
    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    # Change Scaling asepct ratio
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    # Side bar event (called when button clicked)
    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.create_home_screen()
    app.mainloop()



