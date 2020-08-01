# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:16:05 2020

@author: hicks
"""

orString = input("Enter a word to convert into pig latin :")

vowels = ["a", "e", "i", "o", "u", "y"]
pigString = ""
x = len(orString)-1
y = 1

if orString[0] in vowels:
    pigString = pigString + orString + "yay"
else:   
    while y <= x:     
        pigString = pigString + orString[y]
        y = y + 1
    pigString = pigString + orString[0] + "ay"
        
print(pigString)