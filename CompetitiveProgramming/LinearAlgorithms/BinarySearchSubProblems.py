# Number of itereations of binary search through the given array with odd number of elements

##n = int(input())
##num_of_iter = 0
##def number_of_ierations(index):
##    global num_of_iter
##    num_of_iter += 1
##    
##    # base case
##    if index == (n-1):
##        return #returns None    
##
##    index = (index + n)//2
##    # recursive case
##    number_of_ierations(index)
##
##number_of_ierations( (n-1)//2 )    
##
##print(num_of_iter)
##        
"""
In this problem your task will be to process multiple queries in the form “ﬁnd
the leftmost integer in a sorted array which is not less than a given integer”.
"""

##n,nqueries = [int(x) for x in input().split()]
##arr = [int(x) for x in input().split()]

##for i in range(nqueries):
##    l = -1
##    r = n
##    x = int(input())
##    while l+1 < r:
##        mid = (l + r)//2
##        if arr[mid] < x:
##            l = mid
##        else:
##            r = mid
##    if r < n:
##        print(arr[r])
##    else:
##        print("NO SOLUTION")

"""
In this problem your task will be to process multiple queries in the form “ﬁnd the
leftmost integer in a sorted array which is greater than a given integer”.
"""
##n,nqueries = [int(x) for x in input().split()]
##arr = [int(x) for x in input().split()]
##
##for i in range(nqueries):
##    l = -1
##    r = n
##    x = int(input())
##    while l+1 < r:
##        mid = (l + r)//2
##        if arr[mid] <= x:
##            l = mid
##        else:
##            r = mid
##    if r < n:
##        print(arr[r])
##    else:
##        print("NO SOLUTION")
##
"""
In this problem your task will be to process multiple queries in the form “ﬁnd the
index of the rightmost integer in a sorted array which is less than a given integer”. Note that in this task indices are 1-based.

"""
##n,nqueries = [int(x) for x in input().split()]
##arr = [int(x) for x in input().split()]
##
##for i in range(nqueries):
##    l = -1
##    r = n
##    x = int(input())
##    while l+1 < r:
##        mid = (l + r)//2
##        if arr[mid] < x:
##            l = mid
##        else:
##            r = mid
##    if l > -1:
##        print(l+1)
##    else:
##        print("NO SOLUTION")

"""
In this problem your task will be to process multiple queries in the form “ﬁnd the index of the leftmost integer in a non-increasing array
which is less than or equal to a given integer”. Note that in this task indices are 1-based.
"""

n,nqueries = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

for i in range(nqueries):
    l = -1
    r = n
    x = int(input())
    while l+1 < r:
        mid = (l + r)//2
        if arr[mid] > x:
            l = mid
        else:
            r = mid
    if r < n:
        print(r+1)
    else:
        print("NO SOLUTION")


