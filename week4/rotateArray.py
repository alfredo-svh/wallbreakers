class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==len(nums):
            return
        if k > len(nums):
            k = k%len(nums)
            
        k = len(nums) - k
        
        for i in range(k):
            nums.append(nums.pop(0))