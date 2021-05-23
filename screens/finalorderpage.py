import tkinter as tk
from tkinter import font as tkfont # python 3
from tkinter import ttk
from pizzapy.menu import *
from pizzapy.order import *
from pizzapy.payment import CreditCard
import pprint 

# choose card or cash
# if card -> 
    # enter card information
    # validate the card information data
# place the order, give eta


class FinalOrderPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.back_button = ttk.Button(self, text = "Go Back", command = self.back)
        self.back_button.place(x = 0, y = 0, width = 200, height = 100)
        self.back_button.pack()
        # card number, expiration date (mm/yy), 3 digit cvv, zip code"
        self.card_number = tk.Entry(self, textvariable = tk.StringVar())
        self.card_number.insert(0, "ENTER CREDIT CARD NUMBER HERE")
        self.card_number.pack(side= "top")

        self.expiration_date = tk.Entry(self, textvariable = tk.StringVar())
        self.expiration_date.insert(0, "Enter Expiration Date (MMYY) Here")
        self.expiration_date.pack(side= "top")

        self.cvv = tk.Entry(self, textvariable = tk.StringVar())
        self.cvv.insert(0, "Enter CVV Here")
        self.cvv.pack(side= "top")
        
        self.zip_code = tk.Entry(self, textvariable = tk.StringVar())
        self.zip_code.insert(0, "Enter Zip Code Here")
        self.zip_code.pack(side= "top")

        self.init_credit_button = ttk.Button(self, text = "Verify Card Info", command = self.verify_card_info)
        self.init_credit_button.pack()


    def back(self):
        self.controller.show_frame("OrderReviewPage")

    def verify_card_info(self):
        # get the information from the Entries
        # verify the information by making a credit card out of it
        # return true
        print("verifying card info...\n")
        
        user_entered_num = self.card_number.get().strip().replace("-","")
        user_entered_date = self.expiration_date.get().strip().replace("/", "")
        user_entered_cvv = self.cvv.get().strip()
        user_entered_zip = self.zip_code.get().strip()

        # try to validate the credit card
        try:
            self.card = CreditCard(user_entered_num, user_entered_date, user_entered_cvv, user_entered_zip)
            
            # if we get to this point, that means we successfully made the credit card
            self.creditmessage = tk.Label(self, text = "your credit card was accepted, please move on.")
            confirm_order = ttk.Button(self, text= "Confirm Order", command = self.order_sender)
            confirm_order.pack(side= "bottom")
            self.creditmessage.pack(side= "top")
        # if we fail to make the credit card because information is invalid..

        except Exception as e:
            print(e)
            self.error = tk.Label(self, text= "Invalid credit card info")
            self.error.pack(side = "top")

    def order_sender(self): 
        # Order(store, customer, country="us"):
        my_order = Order(self.controller.client.chosen_rst, self.controller.client)
        # loop through our cart and add items to the order
        for item in self.controller.client.cart:
            my_order.add_item(item.code)
        print("\n\n TRYING ORDER NWO")
        try:
            # my_order.place(self.card)
            pprint(my_order.place(self.card))
            print("Successful placement!")

        except Exception as error:
            print("\n ERROR HAPPENED: \n")
            print(error)
            # make a label that tells user the order failed to send






        

