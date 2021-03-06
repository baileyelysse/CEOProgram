"""
title: while loops
author: Bailey Patterson
date: 7/19/18 2:19 PM
"""


import random


def guess_number(low, high):
    guess = input(f"Give number between {low} and {high}: ")
    guess = int(guess)3
    comp_guess = random.randint(low, high)

    if guess < low:
        return f"No, {guess} is less than {low}."
    elif guess > high:
        return f"No, {guess} is higher than {high}"
    guess_num = 1

    while guess != comp_guess:
        guess = int(input("Incorrect. Try again: "))
        guess_num += 1

    print(f"correct! It took you {guess_num} guesses to guess my number, {comp_guess}!")


print (guess_number(1, 5))