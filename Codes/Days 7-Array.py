#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    #print(arr)
    #print(arr[1], arr[len(arr)-2])
    swap1 = 0
    swap2 = 0
    for i in range( int((len(arr)) /2)):
        swap1 = arr[i]
        swap2 = arr[len(arr)-i-1]
        #print(arr[i], arr[len(arr)-i-1])
        arr[i] = swap2
        arr[len(arr)-i-1] = swap1
    #print(arr)
    print(' '.join(map(str, arr)))