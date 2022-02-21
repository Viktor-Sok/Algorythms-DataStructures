# return the index of the leftmost value of 1 in arr = [000011111]
n,nsteps = [int(x) for x in input().split()]
mid_values_arr = [int(x) for x in input().split()]
l = -1 #left index (val = 0)
r = n #right index (val = 1)
for k in range(nsteps):
    index = (l+r)//2
    if mid_values_arr[k] == 0:
        l = index
    else:
        r = index
print(r)        
        
