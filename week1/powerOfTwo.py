class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <1:
            return False
        
        for i in range(n):
            r = pow(2,i)
            if r==n:
                return True
            if r> n:
                return False