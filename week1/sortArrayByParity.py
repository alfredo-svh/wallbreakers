class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []; odds = []
        
        for i in A:
            if i % 2==0:
                even.append(i)
            else:
                odds.append(i)
            
        return even + odds