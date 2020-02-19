class Solution:
    def firstUniqChar(self, s: str) -> int:
        ms = collections.Counter(s)
        
        for i in range(len(s)):
            if ms[s[i]] == 1:
                return i
        
        return -1