class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        cookie = 0
        
        for i in range(len(g)):
            while cookie < len(s) and s[cookie] < g[i]:
                cookie+=1
            
            if cookie == len(s):
                return i
            
            cookie+=1
        
        
        return len(g)