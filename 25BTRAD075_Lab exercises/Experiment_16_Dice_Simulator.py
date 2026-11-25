# LAB EXERCISE 16: Dice Simulator Using Random Module

import random

n = int(input("Enter number of rolls: "))

for i in range(n):
    dice = random.randint(1, 6)
    print("Roll", i + 1, ":", dice)
