# https://practice.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1/?track=md-arrays&batchId=144

# method-1: O(n**2)
def maxLen(arr, N):
    maxl=-1
    sum=0
    for i in range(N):
        sum = -1 if arr[i]==0 else 1
        for j in range(i+1,N):
            sum+= -1 if arr[j]==0 else 1
            if sum==0 and maxl<j-i+1:
                maxl = j-i+1
    if maxl==-1:
        return 0
    return maxl
ans=maxLen([1,0,1,0],4)
print(ans)  

# method-2 : O(n)

def maxLen(arr, n): 
	hash_map = {} 
	curr_sum = 0
	max_len = 0

	for i in range (0, n): 
		if(arr[i] == 0): 
			arr[i] = -1
		else: 
			arr[i] = 1

	for i in range (0, n): 
		curr_sum = curr_sum + arr[i] 
		
		if (curr_sum == 0): 
			max_len = i + 1
			
		if curr_sum in hash_map:
			if max_len < i - hash_map[curr_sum]:
				max_len = i - hash_map[curr_sum]
		else: 
			hash_map[curr_sum] = i 

	return max_len

