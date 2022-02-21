n = int(input())
cur, a, b = [int(x) for x in input().split()]

def get_arr():
	mod = 1791791791   
	global cur 
	cur = (cur * a + b) % mod  
	return cur  
arr = [get_arr() for i in range(n)]

max_val = max(arr)
indx1 = arr.index(max_val)
while True:
	
	if (len(arr) >= indx1 + 1) and (arr[indx1] == max_val):			
		arr.pop(indx1)
	else:
		break
indx2 = arr.index(max(arr))
print(indx1 + 1, indx2 + 1)
