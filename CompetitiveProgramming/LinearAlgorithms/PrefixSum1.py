# Print for defined number of queries the sum between l and r indexes inclusive
n, nqueries = tuple([int(x) for x in input().split()])
arr = [int(x) for x in input().split()]
Part_sum = [0]
for i,elem in enumerate(arr):
    Part_sum.append(Part_sum[i] + elem)

while nqueries > 0:
    l,r = tuple([int(x) for x in input().split()])
    print(Part_sum[r] - Part_sum[l-1])
    nqueries -=1
    
