import tkinter as tk
from tkinter import font as tkfont # python 3
from tkinter import ttk
from pizzapy.menu import *
from pizzapy.order import *


#1. list the whole order and price
#2. Special requests box
    # - insert a tk.Entry that allows users to type in a special request/ notes
    # - save whatever a user typed into the box into a variable
    # - save that variable into the client

#3. Go back
#4. Finalize Order and Pay

class OrderReviewPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.show_cart_button = ttk.Button(self, text = "Show Your Order", command = self.show_cart)
        self.show_cart_button.pack(side = "top")

        self.back_button = ttk.Button(self, text = "Go Back", command = self.back)
        self.back_button.place(x = 0, y = 0, width = 200, height = 100)
        self.back_button.pack()
            
        self.special_requests = tk.Entry(self, textvariable = tk.StringVar())
        self.special_requests.pack(side= "left")

        self.move_to_next_slide = ttk.Button(self, text = "Finalize Order", command = self.move_to_next_page)
        self.move_to_next_slide.pack()

    def move_to_next_page(self):
        self.controller.show_frame("FinalOrderPage")


    def show_cart(self):
        cart_label = ""
        for item in self.controller.client.cart:
            cart_label = cart_label + item.name + " $" + str(item.price) + "\n"
        tk.Label()
        self.menu = tk.Label(self, text = cart_label)
        self.menu.pack()

    def done(self):
        for item in self.controller.client.cart:
            self.controller.client.order.add_item(item)

    def back(self):
        self.controller.show_frame("OrderPage")

