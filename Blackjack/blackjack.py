#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:39:02 2024

@author: anirudhkulkarni
"""

# Check out the README to try the game and for the rules of the game.


# Import libraries
import random
import os


# Function to pick the next card
def pick_another_card(player_cards, comp_cards):
    user_inp2 = input("Type 'y' to get another card, type anything else to pass:\n\n")
    if user_inp2 == 'y':
        player_cards.append(cards[random.randint(0, len(cards)-1)])
        check_for_ace(player_cards)
        current_player_score = sum(player_cards)
        print(f'Your cards: {player_cards}') 
        print(f'Your current score: {current_player_score}')
        print(f"Computer's first card: {comp_cards[0]}")

        if current_player_score <= 21:
            pick_another_card(player_cards,comp_cards)
    
# Function that calculates the value of Ace - either 1 or 11        
def check_for_ace(cards_to_check):
    if (11 in cards_to_check) and (sum(cards_to_check)>21):
        cards_to_check[cards_to_check.index(11)]=1
    return cards_to_check
    
# End game - check who is the winner.
def final_decision(player_cards, comp_cards):
    comp_cards = check_for_ace(comp_cards)
    player_cards = check_for_ace(player_cards)
    
    while sum(comp_cards) < 16:
        comp_cards.append(cards[random.randint(0, len(cards)-1)])
        comp_cards = check_for_ace(comp_cards)
    
    player_score = sum(player_cards)
    comp_score = sum(comp_cards)

    str1 = f'\nYour final hand: {player_cards} \nYour final score: {player_score}.\n'
    str2 = f"Computer final hand: {comp_cards} \nComputer's final score: {comp_score}.\n"
           
    final_str = ''
    if player_score > 21:
         final_str = str1 + str2 + '\nSorry, you lose as you have gone overboard.'
    elif comp_score > 21:
        final_str = str1 + str2 + '\nComputer has gone overboard. Congrats, you win!'
    elif player_score < comp_score:
        final_str = str1 + str2 + '\nSorry, you lose as you have a lower score.'
    elif player_score > comp_score:
        final_str = str1 + str2 + '\nCongrats! You win as you have a higher score.'
    else:
        final_str = str1 + str2 + "\nIt's a draw."
        
    print(final_str)

# List of the values of the different cards in the game    
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_inp = input("Do you want to play a game of Blackjack? Type 'y' for yes. Otherwise, type anything else to quit. \n\n")


while user_inp == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    player_cards = [cards[random.randint(0, len(cards)-1)], cards[random.randint(0, len(cards)-1)]]
    comp_cards = [cards[random.randint(0, len(cards)-1)], cards[random.randint(0, len(cards)-1)]]

    current_player_score = sum(player_cards)
    current_comp_score = sum(comp_cards)

    print(f'Your cards: {player_cards}') 
    print(f'Your current score: {current_player_score}')
    print(f"Computer's first card: {comp_cards[0]}")

    pick_another_card(player_cards, comp_cards)
    final_decision(player_cards, comp_cards)

    user_inp = input("Do you want to play another game now? Type 'y' for yes. Otherwise, type anything else to quit. \n\n")

else:
    print("\nThat's cool. Have a nice day.")


























