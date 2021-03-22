
#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr = list(itertools.chain.from_iterable(itertools.repeat(values[i], freqs[i])
    for i in range(n)))
    arr.sort()
    #print(arr)
    N = len(arr)
    #print(N)
    mid = int(N/2)
    #print(mid)
    #MEDIAN Q2
    #Q2 = int((arr[mid-1]+arr[mid])/2 if n%2 == 0 else arr[mid])
    
    #Lower
    L = arr[0:mid]
    #print(L)
    nL = len(L)
    midL = int(nL/2)
    #print(midL)
    #Q1
    Q1 = round((L[midL-1]+L[midL])/2 if nL%2 == 0 else L[midL],1)
    #print(Q1)
    
    #Upper
    U = arr[mid if n%2== 0 else mid+1:]
    #print(U)
    nU = len(U)
    midU= int(nU/2)
    #print(midU)
    #Q3
    Q3 = round((U[midU-1]+U[midU])/2 if nU%2 == 0 else U[midU],1)
    #print(Q3)

    print(float(Q3-Q1))
    
    
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
