from pizzapy.address import Address
from tkinter import Tk, Label, Button, StringVar
from pizzapy.payment import CreditCard


class Client():
    def __init__(self):
        self.name = ""
        self.address = Address("", "", "", "", "", "us")
        self.phone = ""
        self.place = ""
        self.method = "Delivery"
        self.card = ""
        self.items = []
        self.total_price = 0
        self.order = None
        self.chosen_rst = None
        self.first_name = ""
        self.last_name = ""



