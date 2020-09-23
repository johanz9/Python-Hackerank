"""
Given N integers, counts total pairs of integers with a difference of K.
https://www.hackerrank.com/challenges/pairs
"""

import math
import os
import random
import re
import sys


# Complete the pairs function below.
def pairs(k, arr):
    pair = 0
    """for i in arr:
        for j in arr:
            if (i-j) == k:
                pair += 1"""

    distinct = set(arr)
    # print(distinct)

    for number in arr:
        difference = number - k
        # print(difference)

        if difference in distinct:
            pair += 1

    return pair


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()