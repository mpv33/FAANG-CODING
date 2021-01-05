# Q; https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1/?track=md-arrays&batchId=144

# method-1 : n**2
def majorityElement(A,N):
    target=N//2
    for i in A:
        if A.count(i)>target:
            return i
    return -1

# method 2: n

def majorityElement(arr,size):
    m = {} 
    for i in range(size):
        if arr[i-1] in m:
            m[arr[i-1]]+=1
        else:
            m[arr[i-1]]=1
        
    count = 0
    for key in m: 
        if m[key] > size // 2: 
            count = 1
            return key
            
    if(count == 0): 
        return -1


# method-3.....n
from collections import Counter
def majorityElement(arr,n):
    ct = Counter(arr)
    found = -1
    for key, value in ct.items():
        if value > n//2:
            found = key
            break
    return found