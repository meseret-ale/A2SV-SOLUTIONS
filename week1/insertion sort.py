#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    x = 0
    for i in range(n):
        for j in range(n):
            x = n-j-1
            if n-2-j>=0 and(arr[x] < arr[x-1]):
                y=arr[x]
                arr[x] = arr[n-2-j]
                print(*arr)
                arr[n-2-j] = y
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
