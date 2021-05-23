# HIGH LEVEL EXPLNAATION OF PROJECT
"""
A GUI app that uses the Dominoes API to allow users to order pizza to anywhere.

GUI: Graphical User Interface

Process of ordering a pizza EASILY

1. get the customers name, address, basic information
2. choose a store (probably the closest) 
3. Choosing the pizza
    - chooose toppings/type, etc. 
    - search feature? 
    - add to a cart

4. Review order
5. payment
6. PIZZA COMES TO HOUSE


assignment 10-18-20:
- using the above ordering flow, come up with what screens/feature you will need in your app.
- what API functions from Dominoes do we need? How might we use them? Come up with a few (ish). 


1. Accept Credit Card
    -> validate_credit_Card(card_number, expiration):
        - makes sure that card_number is a real credit card

2. Accept/Submit Order
    -> send the final order through:
        final_send_order(order, customer):
            - makes sure that the restaurant recieves our order and starts making it

3. Customize orders
    -> defined by us. 
    
4. Menu Options
    -> search_menu_options(keyword):
        - return all the items in the menu that have this keyword

5. Trigger Delivery
    ->  finalize the order -> starts delviery

"""

# OOP/OOD Object Oriented Programming/Design

# 1. functions
# 2. data structures (Arrays, map, tuple)
# 3. files (might use this to organize/separate code)
"""
1. Objects

Object exmaple: Utensil

types of utensils are: spoon, fork, knife, spatula, ladle, whisk, chopsticks, spork


                    Utensil
                    /     \
                spoon    fork           
                /   \      |
        soupspoon  spork  spork


spoon inherits from Utensil
soupspoon inherits from soupspoon
"""

class Utensil():
    usage
    color
    material
    thickness
    weight
    length
    mass

class Knife(Utensil):
    sharpness
    blade_length
    def cut(some_food):
        # here we do cutting stuff
        # cut some_food into pieces
        return

class Fork(Utensil):
    pointiness
    number_of_points

class Spoon(Utensil):
    Roundness
    volume_of_storage
    bend_angle
    fullness = 0
    def scoop_full(some_liquid):
        # here we scoop some liquid
        fullness = 100
        return 

class Spork(Spoon, Fork):


    






    




