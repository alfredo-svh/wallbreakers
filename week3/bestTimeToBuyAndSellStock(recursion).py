class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        def helper(i, mem, prices, mn):
            if i == len(prices)-1:
                return max(0, prices[i]-mn)
            
            mn = min(mn, prices[i])
            
            if i not in mem:
                mem[i] = max(prices[i]-mn, helper(i+1, mem, prices, mn))
            
            return mem[i]
        
        
        
        if len(prices)<2:
            return 0
        
        mem = {}
        mn = prices[0]
        return helper(1, mem, prices, mn)