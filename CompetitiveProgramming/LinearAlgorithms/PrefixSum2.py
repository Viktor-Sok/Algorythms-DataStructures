# Max sum of elements in array segment
n = int(input())
arr = [int(x) for x in input().split()]
partSum = [0]
for i,elem in enumerate(arr):
    partSum.append(partSum[i] + elem)
maxSegment = -10E9
for  i,elem in enumerate(partSum[1:]):
    temp = elem - min(partSum[:i+1])
    if temp > maxSegment:
        maxSegment = temp

print(maxSegment)
