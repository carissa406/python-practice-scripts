# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:16:05 2020

@author: hicks
"""

orString = input("Enter a word to convert into pig latin :")

vowels = ["a", "e", "i", "o", "u", "y"]
pigString = ""
x = len(orString)-1

k = 0

beginCon = ""

if orString[k] not in vowels:
    while orString[k] not in vowels:
        beginCon += orString[k]
        k+=1
    while k <= x:    
        pigString += orString[k]
        k+=1
    pigString += beginCon + "ay"
    
else:
    pigString += orString + "yay"

print(pigString)
