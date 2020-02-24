class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        
        c = 0
        
        for i in t:
            if i==s[c]:
                c+=1
            
            if c == len(s):
                return True
        
        return False