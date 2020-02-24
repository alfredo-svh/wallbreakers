class Solution:
    def rec(self,x, n):
        if n==1:
            return x
        if n==0:
            return 1

        halfRes = self.rec(x,n//2)

        if n%2==1:
            return x*halfRes*halfRes

        return halfRes* halfRes


    def myPow(self,x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = 0-n

        return self.rec(x,n)