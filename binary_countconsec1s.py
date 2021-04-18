import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    bin = list()
    i = 0
    while True:
        if n/2 == 0:
            break
        elif n/2 != 0:
            bin.append(n%2)
            n = int(n/2)
    bin.reverse()
    
    consec = 0
    maxi = list()
    
    for i in bin:
        if i == 1:
            consec = consec+1
            
        elif i == 0:
            maxi.append(consec)
            consec = 0
        
    maxi.append(consec)
    
    maximum = 0
    for i in maxi:
        if maximum < i:
            maximum = i
    print(maximum)
