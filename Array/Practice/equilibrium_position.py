

# method -1 :  n**2


# method -2 :  o(n)
 
def equilibriumPoint(arr, N):
    total_sum = sum(arr) 
    leftsum = 0
    for i, num in enumerate(arr): 
        total_sum -= num 
        if leftsum == total_sum: 
            return i+1 
        leftsum += num 
       
    return -1