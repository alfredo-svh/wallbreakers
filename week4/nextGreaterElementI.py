class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = []
        mp = {}
        
        for i in range(len(nums2)):
            
            while len(stack)>0 and stack[-1] < nums2[i]:
                mp[stack.pop()] = nums2[i]
            
            stack.append(nums2[i])
            
            
        for num in nums1:
            if num in mp:
                res.append(mp[num])
            else:
                res.append(-1)

        
        return res
    
    # m: nums1, n: nums2
    # time: O(m + nlogn)
    # space: O(m + n)