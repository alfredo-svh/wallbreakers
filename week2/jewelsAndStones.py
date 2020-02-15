class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        res = 0
        
        for i in S:
            if i in J:
                res+=1
                
        return res