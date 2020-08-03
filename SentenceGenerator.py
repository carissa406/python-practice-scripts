# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 16:35:12 2020

@author: hicks
"""
import random

noun = [" dog ", " cat ", " bird ", " tree ", " human "]
articles = ["A", "The"]
midArticle = ["a ", "the "]
verb = ["ate ", "drank "]
adjective = ["smelly ", "delicious ", "gross ", "pretty "]
finNoun = ["burger.", "hot dog.", "door.", "fan."]

print(random.choice(articles) + random.choice(noun) + random.choice(verb) + 
      random.choice(midArticle) + random.choice(adjective) + random.choice(finNoun))