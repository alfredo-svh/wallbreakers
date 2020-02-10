class Solution:
    def binaryGap(self, N: int) -> int:
        mx = 0
        t = 0
        
        nbin = bin(N)[2:]
        
        for i in range(len(nbin)):
            if(nbin[i])=="1":
                if i-t > mx:
                    mx = i-t
                t=i
                    
        return mx