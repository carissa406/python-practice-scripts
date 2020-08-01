# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:05:09 2020

@author: hicks
"""

orString = input("Enter a string: ")
newString = ""
x = len(orString)-1

while x >= 0:
    newString += orString[x]
    x = x-1
    
print(newString)