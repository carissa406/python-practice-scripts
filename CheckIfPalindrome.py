# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 22:22:13 2020

@author: hicks
"""

orString = input("Enter a word for palindrome validation: ")

noSpaces = ""
newString = ""
x = len(orString)-1
y = len(orString)-1

while x >= 0:
    newString += orString[x]
    x = x-1


if newString == orString:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")