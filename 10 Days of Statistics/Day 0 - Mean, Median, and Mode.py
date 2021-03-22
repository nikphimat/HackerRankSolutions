
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
#print(N)
X = input()
X_list = str.split(X," ")
X_list = map(lambda x: int(x), X_list)
X = list(X_list)
#print(list(X_list))

##MEAN
mean = sum(X)/N
print(mean)

##MEDIAN
X.sort()
mid = int(N/2)
#print(mid)
median = (X[mid-1]+X[mid])/2 if N%2 == 0 else X[mid]
print(median)

##MODE
X_count = list(map(lambda x: X.count(x), X))
#print(X_count)
max_ct = max(X_count)
# if x==max_ct else 1
X_select = []
for x in range(N):
    #X_select.append(x) if X_count[x]==max_ct else continue
    if X_count[x]==max_ct:
        X_select.append(x) 
    else:
        continue

#X_select = list(map(lambda x: X_count.index(max_ct), X_count))
print(X[X_select[0]])

