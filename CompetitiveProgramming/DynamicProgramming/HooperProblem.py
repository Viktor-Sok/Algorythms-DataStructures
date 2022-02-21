# Hopper problem (Dynamic Programming)
n = int(input())
arr = [int(x) for x in input().split()]
candies = [0]*(n+1) #max number of candies up to i-th cell
# Base
candies[0] = 0 #
candies[1] = arr[0]
#Dynamics
for i in range(2,n+1):
    candies[i] = max(candies[i-2], candies[i-1]) + arr[i-1]

print(candies[n])
