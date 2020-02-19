class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        m = collections.Counter(t) -  collections.Counter(s)
        
        return list(m.elements())[0]