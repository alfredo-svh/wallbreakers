class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<2:
            return True
        
        j=len(s)-1
        
        for i in range(len(s)):
            
            if not s[i].isalnum():
                if i>=j:
                    return True
                continue
            while not s[j].isalnum():
                if j<=i:
                    return True
                j-=1
            
            if s[i].lower()!=s[j].lower():
                return False
            
            
            j-=1
            
        return True