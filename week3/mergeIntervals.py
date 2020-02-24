class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return []
        
        res = []
        intervals.sort(key = lambda x: x[0])
        
        l = intervals[0][0]
        r = intervals[0][1]
        
        i=1
        
        while True:
            while(i< len(intervals) and intervals[i][0]<= r):
                r = max(intervals[i][1], r)
                i+=1
                
            res.append([l,r])
            
            if not i<len(intervals):
                return res
            l = intervals[i][0]
            r = intervals[i][1]