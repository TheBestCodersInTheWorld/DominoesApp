
import tkinter as tk
from tkinter import font as tkfont # python 3
from tkinter import ttk
from pizzapy.address import *
class InfoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Please Enter Your Information")
        label.pack()
        self.message = tk.Label(self, text = "Please Enter Your First and Last Name")
        self.message.pack()
        self.info_entry = tk.Entry(self, textvariable = tk.StringVar())
        self.info_entry.bind('<Return>', lambda event: self.get_name())
        self.info_entry.pack()
        self.full_addr = None
        self.yes_button = None
        self.number_msg = None
        self.email_msg =  None
        self.next_page = None
        self.entry_label = None


    def get_name(self):
        name = self.info_entry.get()
        name_list = name.split()
        self.controller.client.first_name = name_list[0]
        self.controller.client.last_name = name_list[1]

        # local address 
        self.address_msg = tk.Label(self, text = "Please Enter Your Local Address (HOUSE #, Full Street Name)")
        self.address_msg.pack()
        self.local_entry = tk.Entry(self, textvariable = tk.StringVar())
        self.local_entry.insert(0, "6431 Belmont Street")

        self.local_entry.pack()

        #  City 
        self.city_msg = tk.Label(self, text = "Please Enter Your City")
        self.city_msg.pack()
        self.city_entry = tk.Entry(self, textvariable = tk.StringVar())
        self.city_entry.insert(0, "Houston")

        self.city_entry.pack()
        
        # State 
        self.state_msg = tk.Label(self, text = "Please Enter Your State")
        self.state_msg.pack()
        self.state_entry = tk.Entry(self, textvariable = tk.StringVar())
        self.state_entry.insert(0, "TX")

        self.state_entry.pack()
        
        # Zip/Postal Code 
        self.zip_message = tk.Label(self, text = "Please Enter Your Zip/Postal Code")
        self.zip_message.pack()
        self.zip_entry = tk.Entry(self, textvariable = tk.StringVar())
        self.zip_entry.insert(0, "77005")
        self.zip_entry.pack()

        # test code
        # self.local_entry.insert(0, "5151 Edloe Street")
        # self.city_entry.insert(0, "Houston")
        # self.state_entry.insert(0, "TX")
        # self.zip_entry.insert(0, "77005")
        

        next_button = ttk.Button(self, text= "Next", command = lambda: self.get_address())
        next_button.pack(side="bottom")
      

        # save the name in the text box in the app
        # move on to the next information
    def get_address(self):  
        local = self.local_entry.get()
        city = self.city_entry.get()
        state = self.state_entry.get()
        zip = self.zip_entry.get()
        # if not local or not city or not state or not zip:
        #     print("err")
        full_address = str(local) + ", " + str(city) + ", " + str(state) + ", " + str(zip)
        # self.controller.client.address = full_address


        #AttributeError: 'str' object has no attribute "country code"



        if not self.full_addr:
            self.full_addr = tk.Label(self, text = full_address)
            self.full_addr.pack()
        else: 
            self.full_addr["text"] = full_address
        if not self.yes_button:
            self.yes_button = ttk.Button(self, text= "Yes, this is correct", command = lambda: self.save_address(local, city, state, zip))
            self.yes_button.pack()

    def save_address(self, street, city, state, zip):
        print("saving address")
        self.controller.client.address = Address(street, city, state, zip, "TX", "us")
        self.get_number()

    def get_number(self):
    #phone number
    # strings
        if not self.entry_label: 
            self.entry_label = tk.Label(self, text="Please enter your phone number, then hit enter")
            self.entry_label.pack(pady = 10)
        self.number_msg = tk.Entry(self, textvariable = tk.StringVar())
        self.number_msg.insert(0, "3468748803")
        self.number_msg.pack()
        self.number_msg.bind('<Return>', lambda event: self.save_phone_number())
    
    def save_phone_number(self):
        self.controller.client.phone = self.number_msg.get()
        if not self.email_msg:
            self.get_email()

    def get_email(self):
        # email address
        self.entry_label = tk.Label(self, text="Please enter your email, then hit enter")
        self.entry_label.pack(pady = 10)
        self.email_msg = tk.Entry(self, textvariable = tk.StringVar())
        self.email_msg.insert(0, "cbk1@rice.edu")
        self.email_msg.pack()
        self.email_msg.bind('<Return>', lambda event: self.save_email())
    
    def save_email(self):
        self.controller.client.email = self.email_msg.get()
        if not self.next_page:
            self.move_to_store_locator()

    
    # move to the next page
    def move_to_store_locator(self):
        self.next_page = ttk.Button(self, text="Move to store locator", command = lambda:self.controller.show_frame("StoreLocatorPage"))
        self.next_page.pack(side="right")
        





        # save the name in the text box in the app
        # move on to the next information

    # def get_phone_number(self):
    #     # save the name in the text box in the app
    #     # move on to the next information

    

    







