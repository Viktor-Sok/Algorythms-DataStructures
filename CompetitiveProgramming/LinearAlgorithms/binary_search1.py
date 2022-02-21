# O(logN) example from best to worst case scenario
n,nqueries = [int(x) for x in input().split()]
#defining invariant arr[l] = 0 , arr[r] = 1

while nqueries > 0:
    k = int(input())
    l = -1 # arr[-1] = 0 in mind
    r = n  # arr[n] = 1 in mind
    count = 0
    while (l + 1) < r:
        mid = (l + r)//2
        count += 1
        if (mid < k):
            l = mid
        else:
            r = mid
            
    print(count)       
    nqueries -= 1
    

