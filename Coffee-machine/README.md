# Coffee Machine Program
![Coffee machine image](coffee_machine.jpg)

Welcome to the Coffee Machine Program! This Python application simulates a coffee machine that allows users to order drinks, check resources, and manage transactions. Enjoy brewing your coffee! ☕

## Table of Contents
- [Features](#features)
- [Files Structure](#files-structure)
- [How to Run](#how-to-run)
- [Usage](#usage)

## Features

1. **Order Drinks**: Users can order espresso, latte, or cappuccino.
2. **Resource Reporting**: The current resources of the coffee machine can be viewed.
3. **Resource Checking**: The program checks if enough resources are available for the requested drink.
4. **Resource Adding**: The user can add resources to the machine - milk, water, or coffee.
5. **Coin Processing**: Users can insert coins to pay for their drink, with change calculated if necessary.
6. **Transaction Handling**: Users are informed if their payment is insufficient or if they receive change.
7. **Turn Off Machine**: The machine can be turned off by entering "off".

## Files Structure

The project consists of the following files:

- `main.py`: The main driver program that interacts with users.
- `menu.py`: Contains the menu of available drinks and their prices.
- `coffee_maker.py`: Manages the coffee machine's resources and operations.
- `money_machine.py`: Handles monetary transactions, including coin processing and profit tracking.

## How to Run

1. Ensure you have Python installed on your machine.
2. Clone this repository or download the files.
3. Open a terminal and navigate to the project directory.
4. Run the program using the command:
   ```bash
   python main.py
   ```

## Usage

1. When prompted, enter the type of coffee you would like: `espresso`, `latte`, or `cappuccino`.
2. If you wish to check the current resources, type `report`, or if you wish to add resources, type 'add'.
3. To turn off the coffee machine, simply enter `off`.
4. Follow the prompts to insert coins and complete your purchase.

