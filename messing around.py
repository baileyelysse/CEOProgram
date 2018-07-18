"""
title: messing around
author: Bailey Patterson
date: 7/18/18 10:31 AM
"""

if 100 > 5:
    print("Bailey is always right")

# What can I do on here???Hm...


name = input("Who is the best at foosball?")

if name != 'Bailey':
    new_name = input("You might want to think again...Who is the best at foosball?")
    if new_name == "Bailey":
        print("Heck Yeah I am!")
    else:
        print("You are no fun. Go away.")
else:
    print("Heck yeah I am")