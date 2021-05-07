#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    br = list()
    pair = 0
    for i in ar:
        if i in br:
            continue 
        b = ar.count(i)
        if int(b / 2) > 0:  
            c = int(b/2)
            pair = pair +  c
        br.append(i)
    return pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

    
