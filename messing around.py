"""
title: messing around
author: Bailey Patterson
date: 7/18/18 10:31 AM
"""

import math
import random


def fill_ticket():
    guess_list = []
    for snickers in range(5):
        num = int(input("Enter a number: "))
        guess_list.append(num)
    return guess_list


def create_string():
    letters = ['O', 'r', 'a', 'n', 'g', 'e', ' ', 'M', 'e', 't', 'h', 'o', 'd']
    string = ''
    for letter in letters:
        string += letter
    return string


def matches(ticket, secret):
    num_matches = 0
    for x in range(5):
        if ticket[x] == secret[x]:
            num_matches += 1
    return num_matches


def short_hand(short):
    short = short.replace('for', '4')
    short = short.replace("too", "2")
    short = short.replace("you", "234")
    short = short.replace('and', '&')
    short = short.replace("You", "234")

    removing = "aeiouAEIOU"
    for letter in removing:
        short = short.replace(letter, "")
    short = short.replace("234", "U")

    print(short)





if __name__ == '__main__':
    # guesses = fill_ticket()
    # print(guesses)
    # print(create_string())
    # secret = [1, 2, 3, 4, 5]
    # print(matches(guesses, secret))
    print(short_hand("the trees for the yard are too green in summer for you"))