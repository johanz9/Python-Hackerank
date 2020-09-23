#!/bin/python3

import math
import os
import random
import re
import sys


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        # Check if x is present at mid
        if arr[mid] < x:
            low = mid + 1
        # If x is greater, ignore left half
        elif arr[mid] > x:
            high = mid - 1
        # If x is smaller, ignore right half
        else:
            return mid
            # If we reach here, then the element was not present
    return -1

def fizzBuzz(n):
    mult3 = []
    mult5 = []
    # Write your code here
    for i in range(1, n + 1):
        mult3.append(3 * i)
        mult5.append(5 * i)
    # print("Finished adding elemnts")
    for i in range(1, n + 1):
        if binary_search(mult3, i) != -1 and binary_search(mult5,i) != -1:
            sys.stdout.write("FizzBuzz\n")
        elif binary_search(mult3, i) != -1:
            sys.stdout.write("Fizz\n")
        elif binary_search(mult5, i) != -1:
            sys.stdout.write("Buzz\n")
        else:
            print(i)

if __name__ == '__main__':
    #n = int(input().strip())

    n = 6000
    #n= 15
    fizzBuzz(n)