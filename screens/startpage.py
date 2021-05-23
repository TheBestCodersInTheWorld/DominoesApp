
import tkinter as tk
from tkinter import font as tkfont # python 3
from tkinter import ttk

# Class representing our start page!
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # START MAKING YOUR LABELS, BUTTONS, ETC. FOR THE WELCOME PAGE HERE

        label = tk.Label(self, text="Welcome to Dominos, Would you like to get started on your order?")
        label.pack(side="top")
        yes_button = ttk.Button(self, text="Start Your Order", command= lambda: self.go_to_order_page())
        yes_button.pack(side="bottom")
        quit_button = ttk.Button(self, text= "Quit", command = parent.quit)
        quit_button.pack(side ="top", pady = 20)
        # self.close_button.pack(pady="5")

    def go_to_order_page(self):
        self.controller.show_frame("InfoPage")
    
