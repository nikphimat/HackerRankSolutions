'''
Task
The probability that a machine produces a defective product is 1/3 . What is the probability that the 1st defect occurs when the 5th item is produced?
'''

import math

if __name__ == '__main__':
    num,den = map(str, input().split())
    n = int(input())
    p = int(num)/int(den)
    q = 1-p
    g_np = (q**(n-1))*(p)
    print(round(g_np,3))
