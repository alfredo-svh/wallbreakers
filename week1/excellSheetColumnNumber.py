class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += (ord(s[len(s)-1-i]) - ord('A')+1) * pow(26,i)
            
        return res