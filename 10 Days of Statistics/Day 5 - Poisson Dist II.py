# Enter your code here. Read input from STDIN. Print output to STDOUT
# Input from stdin
meanX, meanY = [float(num) for num in input().split(" ")]

# Cost
ExpCostA = 160 + 40*(meanX + meanX**2)
ExpCostB = 128 + 40*(meanY + meanY**2)

print(round(ExpCostA, 3))
print(round(ExpCostB, 3))
