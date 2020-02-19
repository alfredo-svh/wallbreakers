class Solution:
    def frequencySort(self, s: str) -> str:
        ms = collections.Counter(s)
        s = ""
        
        for c, n in ms.most_common():
            s+= (c*n)
            
        return s