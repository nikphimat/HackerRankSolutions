'''
Task
The probability that a machine produces a defective product is 1/3 . What is the probability that the 1st defect occurs during the first 5 inspections?
'''

import math

if __name__ == '__main__':
    num,den = map(str, input().split())
    n = int(input())
    p = int(num)/int(den)
    q = 1-p
    g_np = 0
    for i in range(1,n+1):
        g_np += (q**(i-1))*(p)
    print(round(g_np,3))
