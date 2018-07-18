"""
title: data_types
author: Bailey Patterson
date: 7/18/18 10:31 AM
"""


def add_tip(total, tip_percent):
    # Return the total amount including tip
    tip = tip_percent*total
    return total + tip


x = add_tip(30, .2)
x += 5


def age_calculator(current_year, birth_year):
    # returns user's age
    return current_year - birth_year


def mean(a, b, c):
    average = (a + b + c) / 3.0
    return average


def distance(x_one, x_two, y_one, y_two):
    x = (x_one - x_two) ** 2
    y = (y_one - y_two) ** 2
    sum = x + y
    return sum**.5


if __name__ == "__main__":
    print(mean(4, 7, 10))
    print(age_calculator(2018, 2001))
    print(x)

    print(distance(1, 4, 5, 9))