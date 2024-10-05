# This is the coffee machine class. 
# It contains the list of remaining resources and methods to list resources, add resouces, ...
# check if resources and sufficient to make coffee, and finally make coffee itself.

from time import sleep

class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"\nWater: {self.resources['water']} ml")
        print(f"Milk: {self.resources['milk']} ml")
        print(f"Coffee: {self.resources['coffee']} g")
        
    def add(self, machine):
        """Lets the user add resources."""
        self.report()
        input_add = input("What resource would you like to add?\nWater or Milk or Coffee? \n\n")
        if str.lower(input_add) in ["water", "coffee", "milk"]:
            try:
                input_quantity = int(float(input(f"How much {str.title(input_add)} would you like to add? Enter the amount.\n")))
                if input_quantity<0:
                    raise ValueError
                else:
                    self.resources[f"{str.lower(input_add)}"] += input_quantity
                    print("Thank you. Adding ...")
                    sleep(2)
                    self.report()
                    machine.report()
            except ValueError:
                _ = input("Sorry, that's not possible. Hit any key to continue.\n")
    
        else:
                _ = input("Sorry, that's not possible. Hit any key to continue.\n")


    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"\nSorry there is not enough {item}.")
                can_make = False
        if can_make == False:
            _ = input('Hit any key to restart.\n')
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        sleep(2)
        _ = input(f"Here is your {order.name} ☕️. Enjoy! Hit any key to continue.\n")

        
        