import math
import os
import random
import re
import sys

def Multiples(n):
    for i in range(1,11):
        sys.stdout.write(str(n) + " x " + str(i) + " = " + str(n * i)+"\n")


if __name__ == '__main__':
    n = int(input("Insert N: "))
    Multiples(n)