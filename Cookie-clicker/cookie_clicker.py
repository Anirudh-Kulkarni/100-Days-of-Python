#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 13:17:36 2024

@author: anirudhkulkarni
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import schedule 
import time

# Set up Chrome options to keep the browser open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Time intervals for clicking and buying add-ons
click_time = 1  # in minutes
buy_add_on_time = 5  # in seconds

# Initialize the Chrome driver with specified options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the Cookie Clicker game website
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Click the consent button for cookies
consent_button = driver.find_element(By.CLASS_NAME, value="fc-primary-button")
time.sleep(4)  # Wait for the button to load
consent_button.click()

# Select the English language option
lang_button = driver.find_element(By.ID, value="langSelect-EN")
time.sleep(4)  # Wait for the button to load
lang_button.click()

time.sleep(4)  # Wait for the game to load
# Uncomment the line below to prompt for user input
# start_input = input('Ready? Y/N? \n')
start_input = 'Y'  # Automatically set to 'Y' for testing

# Click the cookies acceptance button
cookies_accept_button = driver.find_element(By.CSS_SELECTOR, "a.cc_btn.cc_btn_accept_all")
cookies_accept_button.click()

# Find the main cookie button to click
cookie = driver.find_element(By.ID, value="bigCookie")

# Function to buy an add-on if available
def buy_add_on(): 
    add_on = driver.find_elements(By.CLASS_NAME, 'unlocked')  # Find all unlocked add-ons
    if len(add_on) > 0:  # Check if there are any unlocked add-ons
        add_on[-1].click()  # Click the last unlocked add-on
        print("Bought an add on.")
    
# Function to stop clicking and print cookies per second
def end_clicking(): 
    global keep_clicking  # Use the global variable to control the loop
    keep_clicking = False  # Stop clicking
    cookie_per_s = driver.find_element(by=By.ID, value="cookiesPerSecond").text  # Get cookies per second
    print(cookie_per_s.strip('per second:'))  # Print cookies per second without the text

# Check if the user is ready to start
if start_input == 'Y':
    keep_clicking = True  # Set the clicking flag to true
    schedule.every(buy_add_on_time).seconds.do(buy_add_on)  # Schedule buying add-ons
    schedule.every(click_time).minutes.do(end_clicking)  # Schedule stopping clicking after the specified time
      
    # Main loop for clicking the cookie
    while keep_clicking: 
        schedule.run_pending()  # Run scheduled tasks
        cookie.click()  # Click the cookie
        
else: 
    print("Oops! You did not enter Y. Re-run the program to try again.")

# Close the driver and quit the browser
driver.close()
driver.quit()



