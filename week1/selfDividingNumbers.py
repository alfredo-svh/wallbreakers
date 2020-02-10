class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        res = []
        f = True
        for i in range(left, right+1):
            if i <10:
                res.append(i)
                continue
                
            f = True
            for j in str(i):
                if int(j) == 0 or i%int(j)!=0:
                    f = False
                    break
            if f == True:
                res.append(i)
                
        return res