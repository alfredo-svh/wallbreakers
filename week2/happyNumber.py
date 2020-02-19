class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        
        while n not in s:
            if n == 1:
                return True
            
            s.add(n)
            
            t = str(n)
            n=0
            
            for i in range(len(t)):
                n+= int(t[i])*int(t[i])

        return False