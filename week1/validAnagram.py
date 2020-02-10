class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = {}
        
        for i in s:
            if i in letters:
                letters[i]+=1
            else:
                letters[i]=1
        
        for i in t:
            if not i in letters:
                return False
            letters[i]-=1
            if letters[i] < 0:
                return False
        
        return True