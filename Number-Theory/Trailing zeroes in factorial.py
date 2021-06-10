#Q: https://practice.geeksforgeeks.org/problems/trailing-zeroes-in-factorial5134/1/?track=MD-Math&batchId=144
# Tag:  MakeMyTrip, Microsoft

#m-1
class Solution:
    def trailingZeroes(self, n):
        if(n < 0):
            return -1
        count = 0
         # Keep dividing n by 5 & update Count
        while(n >= 5):
            n //= 5
            count += n
        return count

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input()) 
        ob = Solution()
        ans = ob.trailingZeroes(N)
        print(ans)
