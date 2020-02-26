class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(i, nums, mem, f):
            if i >= len(nums):
                return 0
            
            if i == len(nums)-1:
                if f:
                    return nums[i]
                else:
                    return 0
            
            if i not in mem or mem[i][1]!=f:
                mem[i] = (max(nums[i] + helper(i+2, nums, mem, f), helper(i+1, nums, mem, f)), f)
            
            return mem[i][0]
            
            
            
        if len(nums)==1:
            return nums[0]
        
        mem = {}
        
        return max(helper(0,nums, mem, False), helper(1, nums, mem, True))