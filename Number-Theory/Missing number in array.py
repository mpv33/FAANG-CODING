#Q: https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1/?track=MD-Math&batchId=144
# TAG:  Accolite, Adobe, Amazon, Cisco ,D-E-Shaw, Intuit ,Microsoft, Morgan Stanley ,Ola Cabs ,Payu, Qualcomm ,Visa


class Solution:
    def MissingNumber1(self,array,n):
        ans1=sum(array)
        ans2=(n*n+n)//2
        result=ans2-ans1
        return result
    def MissingNumber2(self,a,n):
       x1 = a[0]
       x2 = 1
       for i in range(1, n-1):
           x1 = x1 ^ a[i]
       for i in range(2, n + 1):
           x2 = x2 ^ i
       return x1 ^ x2
        


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s1=Solution().MissingNumber1(a,n)
    s2=Solution().MissingNumber1(a,n)
    print(s1,s2)
