import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    sum5 = list()
    i = 0
    for i in range(0,4):
        for j in range(0,4):
            sum1 = arr[i][j]+arr[i][j+1]+arr[i][j+2]
            sum2 = arr[i+1][j+1]
            sum3 = arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            sum4 = sum1+sum2+sum3
            sum5.append(sum4)
    sum5.sort()
    print(sum5[15])
