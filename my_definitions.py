'''
Program: my_definitions.py
Author: Joshua M McGinley
Last Date Modified: 10/26/2022


Write a Python module, called my_definitions that includes the following

    A function greeting that prints a friendly greeting
    A function message that prints you as the author of the code
    A function print_dict that accepts a dictionary and prints the pairs (key, value) one per line
    A function print_set that accepts a set and prints the set one item per line

Write a python file called use_definitions_module.py that uses your module.
'''

def greet():
    print("What's happening.")

def author():
    print("Joshua wrote this.")

def print_dict(dict):
    for x, y in dict.items():
        print(x, ":", y)

def print_set(the_set = ()):
    for x in the_set:
        print(x)
