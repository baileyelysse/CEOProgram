"""
title: branching
author: Bailey Patterson
date: 7/18/18 11:53 AM
"""

import math
import random

a = 5
b = 6

print(a >= 3 or b == 3)

# print("Welcome! Our menu consists of Pizza, salad, sushi, fajitas, and omelettes. What would you like?")


def food_order(choice, menu):
    if choice in menu:
        return "Your " + choice + " will be out as soon as possible."
    else:
        input("Please order something on the menu: ")

        if choice in menu:
            return "Your " + choice + " will be out as soon as possible."
        else:
            return "Get out of my restaurant."


def guess_number(low, high):
    guess = input(f"Give number between {low} and {high}: ")
    guess =int(guess)
    if guess < low:
        return f"No, {guess} is less than {low}."
    elif guess > high:
        return f"No, {guess} is higher than {high}"
    else:
        comp_guess = math.floor(random.randint(low, high))
        print(comp_guess)
        if comp_guess != guess:
            return "Oh no, the computer has beaten you!"
        else:
            return "Correct!"


if __name__ == '__main__':
    # menu = ['pizza', 'salad', 'sushi', 'fajitas', 'omelettes']
    # choice = input("Enter your choice of entree: ")
    # print(food_order(choice, menu))
    print(guess_number(1, 5))

