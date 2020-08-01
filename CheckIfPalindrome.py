# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 22:22:13 2020

@author: hicks
"""

orString = input("Enter a word for palindrome validation: ")

noSpaces = ""
newString = ""
x = len(orString)-1

for i in orString:
    if i.isalpha():
        noSpaces += i.lower()

y = len(noSpaces) -1
while y >= 0:
    newString += noSpaces[y]
    y = y-1


if newString == noSpaces:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")