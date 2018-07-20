"""
title: advanced exercises
author: Bailey Patterson
date: 7/19/18 9:53 AM
"""


import random
# lists


def shake_ball():
    future = input("Ask a question about your future... ")
    response = ["Yes definitely", 'As I see it', 'Ask again later', 'Cannot predict now', "Don't count on it", 'Very doubtful', 'Yes',
                'No', "I don't care", "Do what you want", "Who's to say?"]
    return random.choice(response)


# tuples


def gymnast_scores():
    scores = (1, 2, 3, 4, 5)
    print(f"The lowest possible score is {scores[0]}, and the highest possible score is {scores[4]}.")
    print(f"A judge can give a gymnast {random.choice(scores)} points.")


def name_generator(first_list, last_list):
    first_name = first_list
    last_name = last_list
    return f"{random.choice(first_name)} " + f"{random.choice(last_name)}"


def finding_vowels(string):
    vowels = set('aeiouAEIOU')
    if vowels.intersection(string):
        return True
    else:
        return False


def polling_friends():
    fav_animals = {
        'Fariah': '',

    }


if __name__ == '__main__':
    print(shake_ball())
    # print(gymnast_scores())
    # first_list = ['Joe', 'Moe', 'Bo', 'LoLo', 'Zo']
    # last_list = ['Smith', 'Rodriguez', 'Hernandez', 'Doe', 'Phillips']
    # print(name_generator(first_list, last_list))
    # print(finding_vowels("no vowels"))
