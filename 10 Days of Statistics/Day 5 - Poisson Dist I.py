# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

mean = float(input())
val = int(input())

e = math.exp(-mean)
mean_sq_val = mean ** val
k_fact = math.factorial(val)
prob = (mean_sq_val*e)/k_fact
print(round(prob,3))
