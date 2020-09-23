#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

"""
Se i è multiplo di 3 e di 5 print Fizzbuzz
se è solo multiplo di 3 pirnt Fizz
se è multiplo solo di 5 print Buzz
se non è multiplo di nessuno alloraa print i
"""

def fizzBuzz(n):
    mult3 = []
    mult5 = []
    # Write your code here
    for i in range(1, n + 1):
        mult3.append(3 * i)
        mult5.append(5 * i)
    # print("Finished adding elemnts")
    for i in range(1, n + 1):
        if i in mult3 and i in mult5:
            print("FizzBuzz")
        elif i in mult3:
            print("Fizz")
        elif i in mult5:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    #n = int(input().strip())

    n = 6000
    fizzBuzz(n)
