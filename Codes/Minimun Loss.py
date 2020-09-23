import math
import os
import random
import re
import sys
import bisect

# Complete the minimumLoss function below.
def minimumLoss(price):
    ans = float('inf')
    stack = [price[0]] #prendo il primo elemento, poi a questa lista andro a aggiungere i resti degli elementi
    for num in price[1:]: #num = gli elementi della lista price
        if num < stack[0]: #se l'elemto è minore del primo elemento in stack
            ans = min(ans, stack[0] - num) #ans è una variabile che prende il minimo tra se stesso e stack[0] -  num
            stack.insert(0, num) #al primo elemento del stack metto num
        else:
            index = bisect.bisect(stack, num) #bisect mi ordina la lista senza fare un sort in ogni inserimento
            #poi bisect mi ritorna la posizione di un elemento nella lista
            if index < len(stack): #se la posizione è minore alla lunghezza del stack
                ans = min(ans, stack[index] - num)
            stack.insert(index, num)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
