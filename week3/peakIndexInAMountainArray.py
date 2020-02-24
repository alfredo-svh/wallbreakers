class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l = 0
        r = len(A)-1
        
        while(l<=r):
            m = (l+r)//2
            
            if A[m] > A[m-1] and A[m] > A[m+1]:
                return m
            
            #left
            if A[m-1] > A[m]:
                r=m-1
            
            #right
            else:
                l=m+1