# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Objective
In this challenge, we learn about binomial distributions. Check out the Tutorial tab for learning materials!

Task
The ratio of boys to girls for babies born in Russia is 1.09:1. If there is  child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places (i.e.,  format).
'''

import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def p_q(n,r):
    p_r = p**r
    q_r = q**(n-r)
    return p_r*q_r

if __name__ == '__main__':
    p_ratio,q_ratio = map(str, input().split())
    p = float(p_ratio)/(float(p_ratio)+float(q_ratio))
    q = 1-p
    #print(p,q)
    start = 3 ##minimum number of boys
    n = 6 
    b_xnp = 0
    for r in range(start,n+1):
        #print(nCr(n,r),p_q(n,r))
        b_xnp += nCr(n,r)*p_q(n,r)
        #print(round(b_xnp,3))
    print(round(b_xnp,3))
    
