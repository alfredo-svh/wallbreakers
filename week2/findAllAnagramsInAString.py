class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        pc = collections.Counter(p)
        res = []
        
        print(pc)
        
        for i in range(len(s)-len(p)+1):
            sbstr = s[i:i+len(p)]
            
            if pc == collections.Counter(sbstr):
                res.append(i)
                
        return res