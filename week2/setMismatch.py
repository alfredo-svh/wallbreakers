class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ms = collections.Counter(nums)
        
        res = [0,0]
        
        for i in range(1, len(nums)+1):
            if ms[i] < 1:
                res[1] = i
            if ms[i] == 2:
                res[0] = i
            if res[0]!=0 and res[1]!=0:
                return res

#Alternatively, using two multisets:

# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         nms = list(range(1, len(nums)+1))
        
#         ms1 = collections.Counter(nums)
#         ms2 = collections.Counter(nms)
        
#         res = [0,0]
        
#         res[0] = list((ms1 - ms2).elements())[0]
#         res[1] = list((ms2 - ms1).elements())[0]
        
#         return res