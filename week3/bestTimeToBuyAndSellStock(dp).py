class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        
        dp = [0]*(len(prices)+1)
        mn = prices[0]
        
        i=0
        while i<len(prices):
            
            mn = min(mn, prices[i])
            
            dp[i+1] = max(prices[i]-mn, dp[i])
            
            i+=1

        return dp[len(prices)]