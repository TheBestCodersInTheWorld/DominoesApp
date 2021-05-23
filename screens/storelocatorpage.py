
import tkinter as tk
from tkinter import font as tkfont # python 3
from tkinter import ttk
from pizzapy.store import StoreLocator, Store

# 6431 Belmont Street

# Class representing our start page!
class StoreLocatorPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Store Locator")
        label.pack(side="top")
        store_locator_button = ttk.Button(self, text="Find Stores", command= lambda: self.find_store_nearest_me())
        # self.close_button.pack(pady="5")
        store_locator_button.pack(side="bottom")
        store_locator_button.place(x=0, y=0)
   
    #def go_to_order_page(self):
        #self.controller.show_frame("InfoPage")
    
    def find_store_nearest_me(self):
        print(type(self.controller.client.address))
        print(self.controller.client.address)
        stores_list = StoreLocator.nearby_stores(self.controller.client.address)
        open_rst = str(stores_list[0]) if len(stores_list) > 0 else "No stores open near you right now!"
        self.first_store = ttk.Button(self, text=open_rst, command = self.confirm_rst(stores_list[0]))
        # self.prompt = tk.Label(self, text=open_rst, font=self.controller.title_font)
        self.first_store.pack()
        v = tk.StringVar()
        # pick_loc_btn = ttk.Button(self, text="This location looks good", command = self.confirm_rst(stores_list[0]))
        # pick_loc_btn.pack()
        find_btn = ttk.Button(self, text="More stores?", command = self.search_rst(stores_list))
        find_btn.pack()

    def search_rst(self, stores_list):
        # stores_list = [store1, store2, STORE3, STORE1 3R2 ]
        if len(stores_list) == 2:
            store2btn = ttk.Button(self, text=str(stores_list[0]), command = self.confirm_rst(stores_list[0]))
            store2btn.pack()
        else:
            store2btn = ttk.Button(self, text=str(stores_list[1]), command = self.confirm_rst(stores_list[1]))
            store2btn.pack()
            store3btn = ttk.Button(self, text=str(stores_list[2]), command = self.confirm_rst(stores_list[2]))
            store3btn.pack()

    def confirm_rst(self, store):
        print("you selected this restaurant" + str(store))
        self.controller.client.chosen_rst = store
        self.move_to_order_page(store)

    def move_to_order_page(self, store):
        self.prompt = tk.Label(self, text = "you chose this store: \n " + str(store))
        self.next_page = ttk.Button(self, text= "Move on?", command=lambda:self.controller.show_frame("OrderPage"))
        self.prompt.pack()
        self.next_page.pack()


    

  