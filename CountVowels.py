# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 22:05:04 2020

@author: hicks
"""

orString = input("Enter in text to count the vowels: ")
vowels = ["a", "e", "i", "o", "u"]
vowelsList = ""

a =0
e =0
i =0
o =0
u =0

for index in orString:
    if index == "a":
        a += 1
    if index == "e":
        e += 1
    if index == "i":
        i += 1
    if index == "o":
        o += 1
    if index == "u":
        u += 1
    
        
print("There are " + str(a) + " A's")
print("There are " + str(e) + " E's")
print("There are " + str(i) + " I's")
print("There are " + str(o) + " O's")
print("There are " + str(u) + " U's")
total = a+e+i+o+u
print("There are a total of " + str(total) + " vowels.")
