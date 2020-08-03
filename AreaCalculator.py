# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:53:43 2020

@author: hicks
"""

shape = input("Are you calculating the area for a rectangle, square, or triangle? :")

if shape == "rectangle":
    l = float(input("What is the length of the rectangle?: "))
    b = float(input("what is the width of the rectangle?: "))
    area = l * b
    print("The area of the rectangle is " + str(area))
elif shape == "square":
    a = float(input("What is the length of one side?: "))
    area = a * a
    print("The area of the square is " + str(area))
elif shape == "triangle":
    b = float(input("What is the base of the triangle?: "))
    h = float(input("What is the height of the triangle?: "))
    area = 0.5 * b * h
    print("The area of the triangle is " + str(area))