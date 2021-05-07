#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#
def median(b):
    a = len(b)
    b.sort()
    
    
    if (a % 2) == 0:
         c = int(a / 2)
         med = (b[c-1]+b[c])/2 
              
    elif (a % 2) == 1:
        c = int((a-1)/2)
        med = b[c]
        
    return int(med)

def quartiles(arr):
    # Write your code here
    b = list(arr)
    b.sort()
    a = int(len(b))
    x = list()
    y = list()
    z = list
    if a % 2 == 0:
        c = int((a/2) - 1)
        x = (b[:c+1])
        y = (b[c+1:])
        
        q1 = median(x)
        q2 = median(b)
        q3 = median(y)
        
    elif a % 2 == 1:
        c = int((a-1)/2)
        x = (b[:c])
        y = (b[c+1:])
        
        q1 = median(x)
        q2 = b[c]
        q3 = median(y)
    qd = q3 - q1
    return qd
    
def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr = list()
    for i in range(len(values)):
        for j in range(freqs[i]):
            arr.append(values[i])
    a = quartiles(arr)
    return print(float(a))
    
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
