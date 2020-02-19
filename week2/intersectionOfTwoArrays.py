class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        m = set(nums1)
        
        n = set(nums2)
        
        res = []
        
        for i in m:
            if i in n:
                res.append(i)
        
        return res