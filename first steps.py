# -*- coding: utf8 -*-

#print("hello")
"""
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

"""

"""
for x in characters:
    print(x.capitalize())

program = {"quotes": ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."], "characters": ["alvin et les Chipmunks", "Babar", "betty boop", "balimero", "casper", "le chat potté", "Kirikou"]}

program.update({"characters" : ["Alvin", "Père Noël"], "quotes": ["Une citation unique qui sera sauvegardée"]})

"""

"""

functions that work on a list

list.pop(), list.index("go"), list.insert(4, "hjy")
list.remove("hjk"), list.pop(4), list[-1], list.append("hjh")

"""

"""
import random


def get_random_item_in(my_list):
    pos = random.randint(0, len(my_list) - 1)
    item = my_list[pos]
    print(item)
    return " prog is over"


user_answer = input("enter a letter : ")

if user_answer == "B":
    pass
elif user_answer == "C":
    print("C pas la bonne réponse ! Et G pas d’humour, je C...")
else:
    print(get_random_item_in(quotes))
"""

class point:
    def __init__(self, x,y):
        self.__x  = x
        self.__y = y

    def deplace(self, dx, dy):
        self.__x = self.__x + dx
        self.__y = self.__y + dy

    def affiche(self):
        print(self.__x, self.__y)


p = point(1,2)


def squares(x):
    for i in range(x):
        yield i ** 2

f = [x**2 for x in range(5)]


def go(n):
    def gogo(m):
        return n*m
    return gogo


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")

f = lambda x : x**2










