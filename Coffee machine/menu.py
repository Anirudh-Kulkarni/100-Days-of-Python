# This is the menu class. It contains the different items and methods to read the prices, and search for items.

class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="Latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="Espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="Cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_menu(self):
        """Returns all the names of the available menu items and their prices"""
        menu_options = ""
        for item in self.menu:
            menu_options += f"\n {item.name}. Cost: {item.cost} dollars \n"
        return menu_options
    
    def get_items(self):
        """Returns all the names of the available menu items"""
        option_names = ""
        for item in self.menu:
            option_names += f"{item.name}/"
        return option_names

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("\nSorry that item is not available.\n")
