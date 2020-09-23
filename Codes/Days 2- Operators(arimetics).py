import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost *(tip_percent/100)
    tax = meal_cost * (tax_percent/100)
    total_cost = meal_cost + tip + tax
    #total_cost_round = int(total_cost)
    #arrontondare, si fa cosi, prima non mi arrotonda bene. per esempio 12.5 rimane 12, invece qua
    #12.5 --> 13
    total_cost_round = round(total_cost)
    #print(total_cost_round)
    sys.stdout.write(str(total_cost_round))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)