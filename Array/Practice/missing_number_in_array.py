#Q: https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1/?track=md-arrays&batchId=144

# method-1 :

def MissingNumber(array,n):
    total=1
    for i in range(2,n+1):
        total+=i
        total-=array[i-2]
    return total

# method-2 :


def MissingNumber(array,n):
   total_sum=((n)*(n+1))//2
   current_sum=sum(array)
   result=total_sum-current_sum
   return result
