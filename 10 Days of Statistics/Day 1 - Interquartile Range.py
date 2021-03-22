
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = sum(arr)/n
    #print(mean)
    num = []
    for i in range(n):
        #print((arr[i]-mean)**2)
        num.append((arr[i]-mean)**2)
    Sdev = math.sqrt(sum(num)/n)
    print(round(Sdev,1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
