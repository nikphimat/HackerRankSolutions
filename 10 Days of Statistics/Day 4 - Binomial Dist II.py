'''
Task
A manufacturer of metal pistons finds that, on average,  12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

No more than 2 rejects?
At least 2 rejects?
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
    defect_percent,batch = map(str, input().split())
    p = float(defect_percent)/100
    q = 1-p
    #print(p,q)
    start = 0
    threshold = 2 ##defect threshold
    n = int(batch) 
    
    ## no more than 2 rejects    
    b_xnp = 0
    for r in range(start,threshold+1):
        #print(nCr(n,r),p_q(n,r))
        b_xnp += nCr(n,r)*p_q(n,r)
        #print(round(b_xnp,3))
    print(round(b_xnp,3))
    
    ## at least 2 rejects
    b_xnp = 0
    for r in range(threshold,n+1):
        #print(nCr(n,r),p_q(n,r))
        b_xnp += nCr(n,r)*p_q(n,r)
        #print(round(b_xnp,3))
    print(round(b_xnp,3))
