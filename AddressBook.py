# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:18:38 2020

@author: hicks
"""

print("Welcome to your Address Book!")
print("Would you like to get contact info or add a new contact?")
userprompt = input("Type 'C' for contact info, or 'N' to make a new contact: ")

if userprompt == "N":
    filename = input("What is the name of contact?: ")
    phone = input("What is their phone number?: ")
    address = input("What is their address?: ")
    email = input("What is their email?: ")
    f = open(filename, "w+")
    f.write(filename)
    f.write("\nPhone Number: " + phone)
    f.write("\nAddress: " + address)
    f.write("\nEmail: " + email)
    f.close()
    
    print("You have entered all contact information. Here is the contact you have created: \n")
    f = open(filename, "r")
    if f.mode== 'r':
        contact = f.read()
        print(contact)
        f.close()
    
elif userprompt == "C":
    filename = input("What is the name of the contact?: ")
    f = open(filename, "r")
    if f.mode == "r":
        contact = f.read()
        print(contact)
        f.close()
    