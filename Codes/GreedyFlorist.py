import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    #sorted_list = sorted(c, reverse=True)
    c.sort(reverse=True)
    result = 0
    count = 0
    count_loop = k
    for i in c:
        if count_loop == 0:
            count += 1
            count_loop = k

        #print("(" + str(count) + " + " + "1" +" ) "+ " x " + str(i))
        result += (count+1) * i
        count_loop -= 1

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()