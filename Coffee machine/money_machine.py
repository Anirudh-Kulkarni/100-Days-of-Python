# This is the class with details about money. 
# It contains the prices of items and methods to make payments and process change. 

class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")
        _ = input("Hit any key to continue.\n")

    def process_coins(self, cost):
        """Returns the total calculated from coins inserted."""
        print(f"\nPlease insert {cost} dollars. You can pay in quarters (25¢), dimes (10¢), nickles (5¢), and pennies (1¢). \n")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins(cost)
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"\nHere is {self.CURRENCY}{change} in change. Preparing coffee ...\n")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            _ = input("\nSorry that's not enough money. Money refunded. Hit any key to continue.\n")
            self.money_received = 0
            return False
