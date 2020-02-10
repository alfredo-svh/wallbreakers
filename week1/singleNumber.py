class Solution:
    def singleNumber(self, nums: List[int]) -> int:

		#using xor

        if len(nums) <2:
            return nums[0]
        
        if(len(nums)%2==0):
            return -1
        
        x=0
        
        for i in nums:
            x = x^i
            
        return x

'''
		#using dictionary:

		if len(nums) <2:
            return nums[0]
        
        if(len(nums)%2==0):
            return -1
        
        t = {}
        
        for i in nums:
            if i in t:
                t.pop(i)
            else:
                t[i] = 1
        
        return t.popitem()[0]
'''