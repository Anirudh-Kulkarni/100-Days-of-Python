# This program implements a coffee machine. 
# You can buy coffee, add resources, and view remaining resouces. 
# Check out the documentation for more details.

# Import the classes and the libraries. 

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

user_input = ''
menu_machine = Menu() # Contains details about the menu.
cmaker = CoffeeMaker() # Contains details about the coffee machine.
money_details = MoneyMachine() # Contains details about money.

while(True):
    os.system('cls' if os.name == 'nt' else 'clear')
    user_input = input(f'What would you like to drink today? \n\t{menu_machine.get_menu()} \
                       \nEnter "report" to amount of remaining resources and "add" to add resources.\
                       \n\nEnter "off" to turn off the machine.\n\n')

    # Stop the machine
    if user_input == 'off':
        break

    # Add resources  
    elif user_input == 'add':
        cmaker.add(money_details)
    
    # Report on remaining resouces
    elif user_input == 'report':
        cmaker.report()
        money_details.report()
    
    # Make an order
    elif str.lower(user_input) in str.split(str.lower(menu_machine.get_items()),'/'):
        ordered_inp = menu_machine.menu[str.split(str.lower(menu_machine.get_items()),'/').
                                        index(str.lower(user_input))]
        if cmaker.is_resource_sufficient(ordered_inp):
            if money_details.make_payment(ordered_inp.cost):
                cmaker.make_coffee(ordered_inp)
    
    # Not a valid option
    else:
        _ = input('\nSorry that item is not available, try again. Hit any key to continue.\n')

