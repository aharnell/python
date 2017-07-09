#!/usr/bin/python

import random
x = True
while x:
    print(random.choice(["Red", "Green", "Purple", "Yellow", "Blue", "Orange"]))
    r = input("Another? (Y/n)> ")
    if r in ["N", "n"]:
        x = False
    