import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    found = 0
    lonely = 0
    for i in a:
        found = a.count(i)
        if found == 1:
            lonely = i
    return lonely

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()