# Given an array of 0s and 1s. Find the length of the largest subarray with equal number of 0s and 1s.

# Example 1:

# Input:
# N = 4
# A[] = {0,1,0,1}
# Output: 4
# Explanation: The array from index [0...3]
# contains equal number of 0's and 1's.
# Thus maximum length of subarray having
# equal number of 0's and 1's is 4.
# Example 2:

# Input:
# N = 5
# A[] = {0,0,1,0,0}
# Output: 2
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function maxLen() which takes the array arr[] and the size of the array as inputs and returns the length of the largest subarray with equal number of 0s and 1s.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).

# Constraints:
# 1 <= N <= 105
# 0 <= A[] <= 1


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

