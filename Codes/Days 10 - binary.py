#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    #convert integer to binary
    arr = []
    while True:
        temp = n/2
        s = int(temp) - temp
        if s >= 0:
            arr.append(0)
            #print("0")
        else:
            #print("1")
            arr.append(1)
        n = int(temp)

        if n == 0:
            #print("done")
            break
    #print(arr)

    #search max consecutive 1
    count = 0
    countmax = 0
    for i in arr:
        #print("i: ",i)
        if i == 1:
            count +=1
            #print("i == 1", count)
        else:
            #print("encontrado un 0")
            if countmax <= count:
                countmax = count
                #print("count max ",countmax)
            count = 0

        if countmax <= count:
            countmax = count
    #print(countmax)
    sys.stdout.write(str(countmax))