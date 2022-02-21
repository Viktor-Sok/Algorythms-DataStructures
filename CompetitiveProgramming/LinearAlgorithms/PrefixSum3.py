arr = [int(x) for x in input().split()]
partSum = [0]
for i,elem in enumerate(arr):
    partSum.append(partSum[i] + elem)
count = 1
partSum.sort()
print(partSum)
for i in range(1,len(partSum)):
    if partSum[i-1] != partSum[i]:
        count += 1
print(count)    
    
    
