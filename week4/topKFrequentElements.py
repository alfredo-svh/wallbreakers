from heapq import heappop, heappush, heapify

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        mp = {}
        heap = []
        
        heapify(heap)
        
        #populate map
        for num in nums:
            if num not in mp:
                mp[num] = 1
            else:
                mp[num]+=1
        
        #populate heap
        for key, val in mp.items():
            heappush(heap, (-val, key))
        
        #populate res
        for i in range(k):
            res.append(heappop(heap)[1])
            
        return res