class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        
        if len(nums) < 2:
            return False
        
        for i in range(len(nums)):
            if nums[i] in myDict:
                return [myDict[nums[i]], i]
            else:
                myDict[target - nums[i]] = i
                    