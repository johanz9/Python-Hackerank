import math
import os
import random
import re
import sys

"""
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

0 -4 -6 0 -7 -6
-1 -2 -6 -8 -3 -1
-8 -4 -2 -8 -8 -6
-3 -1 -2 -5 -7 -4
-3 -5 -3 -6 -6 -6
-3 -6 0 -8 -6 -7

"""

def hourglass(arr):
    maxi = -9 * 9
    for i in range(6):
        for j in range(6):
            if j + 2 < 6 and i + 2 < 6:
                # arr[i][j] + arr[i][j+1] + arr[i][j+2] == top
                # arr[i+1][j+1] == middle
                # arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2] == bottom
                tmp = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][
                    j + 1] + arr[i + 2][j + 2])
                if tmp > maxi:
                    maxi = tmp
    print(maxi)


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hourglass(arr)
