# Q: https://practice.geeksforgeeks.org/problems/a-simple-fraction0921/1/?track=MD-Math&batchId=144#
# TAG: microsoft,amazon


class Solution:
    def fractionToDecimal(self, n, d):
        if n==0:
            return 0
        sign= -1 if n<0 ^ d<0 else 1
        ans1= n//d
        result=''
        if sign==-1:
            result+='-'
        if n%d==0:
            result+=str(ans1)
            return result
        result+=str(ans1)
        result+='.'
        r=n%d
        m={}
        i=0
        rep=False
        while r>0 and not rep:
            if r in m:
                i=m[r]
                rep=True
                break
            else:
                m[r]=len(result)
            r=r*10
            temp=r//d
            result+=str(temp)
            r=r%d
        if rep:
             result += ")"
             x = result[:i]
             x += "("
             x += result[i:]
             result = x
        return result
           

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        numerator, denominator = input().split()
        numerator = int(numerator); denominator = int(denominator)
        ob = Solution()
        ans = ob.fractionToDecimal(numerator, denominator)
        print(ans)