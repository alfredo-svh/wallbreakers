class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        p = sorted(p)
        res = []
        
        for i in range(len(s)-len(p)+1):
            sbstr = sorted(s[i:i+len(p)])
            
            if p == sbstr:
                res.append(i)
                
        return res