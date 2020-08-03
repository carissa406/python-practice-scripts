# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 16:23:23 2020

@author: hicks
"""

import random

trophy = random.randint(0,100)

guess = input("Guess what number I'm thinking of between 0 and 100: ")

while int(guess) != trophy:
    if int(guess) > trophy:
        guess = input("You're too high, guess again: ")
    else:
        guess = input("You're too low, guess again: ")
    
if int(guess) == trophy:
    print("You are correct!")