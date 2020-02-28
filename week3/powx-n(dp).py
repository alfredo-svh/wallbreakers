class Solution:
    def myPow(self,x: float, n: int) -> float:
        def rec(x, n, dp):
            if n in dp:
                return dp[n]

            halfRes = rec(x,n//2, dp)

            if n%2==1:
                dp[n] = x*halfRes*halfRes
            else:
                dp[n] = halfRes* halfRes

            return dp[n]
    
    
    
        if n<0:
            x = 1/x
            n = 0-n
        
        dp = {}
        dp[0] = 1
        dp[1] = x

        return rec(x,n, dp)