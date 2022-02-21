#sum of elements in array
n = int(input())
arr = [int(x) for x in input().split()]
sum = 0
for elem in arr:
	sum += elem
print(sum)
