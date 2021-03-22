
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr.sort()
    mid = int(n/2)
    print(mid)
    #MEDIAN Q2
    Q2 = int((arr[mid-1]+arr[mid])/2 if n%2 == 0 else arr[mid])
    
    #Lower
    L = arr[0:mid]
    print(L)
    nL = len(L)
    midL = int(nL/2)
    print(midL)
    #Q1
    Q1 = int((L[midL-1]+L[midL])/2 if nL%2 == 0 else L[midL])
    
    #Upper
    U = arr[mid if n%2== 0 else mid+1:]
    print(U)
    nU = len(U)
    midU= int(nU/2)
    print(midU)
    #Q3
    Q3 = int((U[midU-1]+U[midU])/2 if nU%2 == 0 else U[midU])
    
    Q= [Q1,Q2,Q3]
    return Q
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

