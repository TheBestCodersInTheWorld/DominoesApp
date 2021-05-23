
import tkinter as tk
from tkinter import font as tkfont # python 3
from tkinter import ttk
from pizzapy.menu import *
from pizzapy.order import *


# Class representing our start page!
class OrderPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.button_Vars = []
        self.cart = []
        self.total = 0

        self.order = None

        self.cart_label = tk.Label(self, text = "")
        self.cart_label.pack(side = "right")

        # START MAKING YOUR LABELS, BUTTONS, ETC. FOR THE WELCOME PAGE HERE

        label = tk.Label(self, text="Would you like to get started on your order?")
        label.pack(side="top")
        self.add_button = ttk.Button(self, text="add selected to cart", command=self.add_to_cart)
        self.add_button.pack()

        self.search_bar = ttk.Entry(self, textvariable = tk.StringVar())
        self.search_bar.bind('<Return>', lambda event: self.search_menu())
        self.search_bar.pack(side= "top")
        self.checkframe = tk.Frame(self, borderwidth = 10)
        self.checkframe.pack()

        done = ttk.Button(self, text="Done with order?", command = self.move_to_next_page)
        done.pack(side="right")

    def move_to_next_page(self):
        self.controller.show_frame("OrderReviewPage")


    def clearFrame(self, frame):
        # destroy all widgets from frame
        for widget in frame.winfo_children():
            widget.destroy()
            
    def search_menu(self):
        search = self.search_bar.get().strip()
        self.get_menu(search)    
    
    def get_menu(self, search = "Pizza"):
        print("Called")
        if not self.order:
            self.order = Order(self.controller.client.chosen_rst, self.controller.client, "us")
            self.menu = self.controller.client.chosen_rst.get_menu()
        
        # menuBox = tk.Label(self, text=str(self.menu))
        # menuBox.pack()
        
        pizzas = self.menu.search(Name = search)
        pizzaString = ""
        for pizza in pizzas:
            print(pizza.code)
            print(pizza.price)
            print(pizza.name)
            pizzaString  = pizzaString + "Code: " + pizza.code + ", Price: " + pizza.price + ", Name: " + pizza.name + "\n"
        print("Called 2 ")

        # menuBox = tk.Label(self,text=pizzaString)
        # menuBox.pack()

        self.pizzamap = {} 
        self.clearFrame(self.checkframe)
        for pizza in pizzas:
            buttonVar = tk.IntVar()
            pizzaButton = tk.Checkbutton(self.checkframe, text = pizza.name + "  " + pizza.price, variable = buttonVar)
            self.pizzamap[pizza] = [buttonVar, pizzaButton]
        # for pizza, intvar in self.pizzamap.items():
            pizzaButton.pack()



    def add_to_cart(self):
        # pizzamap = {pizza_item_1 : [intvar, checkbutton], pizza_item_2: [intvar, checkbutton], .... .. . . }

        # loop through the items of pizzamap, which are keys and values
        temp_cart = []
        temp_price = 0
        for pizza, pizzabutton_stuff in self.pizzamap.items():
        # for each value, when we looking at the checkbutton, we want to add the key into cart
            # TODO: see if the checkbutton is checked or not
            check_intvar = pizzabutton_stuff[0]
            is_it_checked = check_intvar.get()
            if is_it_checked == 1: # if is checked, add pizza to cart, and add price to total
                print(pizza.name)
                temp_cart.append(pizza)
                if pizza.price:
                    temp_price = temp_price + float(pizza.price)
        for menu_item in temp_cart: 
            self.cart.append(menu_item)
        self.total = self.total + temp_price

        print("This is the cart : \n")
        self.controller.client.cart = self.cart

        print(self.cart) 
        
        item_str = ""
        for pizza_object in self.cart:
            item_str = item_str + pizza_object.name + "\n"
        item_str += "Total Price: " + str(self.total)

        self.cart_label['text'] = item_str




        

# API_LINK = "dominoes.com"
# request_data = "THE MENU WITH THIS, THIS, Coupon Pizza ......."
# requests.get(API_LINK, request_data) ->>>>>>>>>>>> dominoes





