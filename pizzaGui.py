import tkinter as tk
# GUI: Graphical User Interface -> a screen with buttons, text fields, etc., to allow users to interact with the application
from tkinter import font as tkfont # python 3
from tkinter import ttk
from tkinter import Scrollbar
from PIL import ImageTk, Image
# from pizzapy import Customer, StoreLocator, Order, ConsoleInput
# from pizzapy.store import Store, StoreLocator
# from pizzapy.address import Address
# from tkinter import Tk, Label, Button, StringVar
# from pizzapy.payment import CreditCard

from client import Client
from screens.infopage import InfoPage
from screens.storelocatorpage import StoreLocatorPage
from screens.startpage import StartPage
from screens.orderpage import OrderPage
from screens.orderreviewpage import OrderReviewPage
from screens.finalorderpage import FinalOrderPage

def handle_focus_in(entry):
    entry.delete(0, tk.END)
    entry.config(foreground='black')

def handle_focus_out(entry):
    entry.delete(0, tk.END)
    entry.insert(0, "Menu Item")

def handle_enter(entry):
    handle_focus_out(entry)


# Class representing our overall page
class Controller(tk.Tk):

    # Methot that initializes all the stuff we want to see in our welcome page
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.frames = {}
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.total_price = 0.0

        self.client = Client()

        # ADD ALL OTHER PAGES HERE IN THIS List
        for F in [StartPage, InfoPage, StoreLocatorPage, OrderPage, OrderReviewPage, FinalOrderPage]:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        global client
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        if type(frame) == OrderPage:
            frame.get_menu()
        frame.tkraise()

root = Controller()
root.geometry("900x1200")
root.mainloop()