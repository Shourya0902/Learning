import math
import os
import random
import re
import sys

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    a = len(arr)
    brr = list(arr)
    summ = 0
    for i in range (len(brr)):
        summ = summ + brr[i]
    mean = float(summ / a)
    
    c = 0
    for i in brr:
        b = (i - mean)**2
        c = c + b
    
    d = c / a
    e = d**0.5
    return print(e)    
        

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
