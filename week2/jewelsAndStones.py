class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        res = 0
        s = set(J)
        
        for i in S:
            if i in s:
                res+=1
                
        return res