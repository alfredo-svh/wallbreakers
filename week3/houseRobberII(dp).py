class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        
        
        dp0 = {}
        dp1 = {}
        
        dp0[0] = 0
        dp0[1] = nums[0]
        
        dp1[0] = 0
        dp1[1] = nums[1]
        
        i=2
        j = 2
        
        while i<len(nums):
            dp0[i] = max(nums[i-1] + dp0[i-2], dp0[i-1])
            print(dp0[i])
            i+=1
        
        while j<len(nums):
            dp1[j] = max(nums[j] + dp1[j-2], dp1[j-1])
            j+=1
            
        return max(dp0[i-1], dp1[j-1])