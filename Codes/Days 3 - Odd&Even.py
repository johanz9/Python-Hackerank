import math
import os
import random
import re
import sys

"""
Given an integer, N, perform the following conditional actions:
If N is odd, print Weird
If N is even and in the inclusive range of to, print Not Weird
If N is even and in the inclusive range of to, print Weird
If N is even and greater than , print Not Weird

Complete the stub code provided in your editor to print whether or not N
is weird.
"""

if __name__ == '__main__':
    N = int(input("Insert a Number: "))

    if (N%2) != 0:
        print("Weird")
    elif N%2 == 0 and N in range(2,5+1):
        print("Not Weird")
    elif N%2 == 0 and N in range(6,20+1):
        print("Weird")
    elif N%2 == 0 and N > 20:
        print("Not Weird")

print(N%2)