# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:54:29 2020

@author: hicks
"""
file = input("Enter a file path ")
fo = open(file,"r")

contents = fo.read()
splitString = contents.split()
print(len(splitString))

fo.close()