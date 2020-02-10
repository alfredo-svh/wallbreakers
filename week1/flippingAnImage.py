class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        temp = []
        
        for i in A:
            temp = i.copy()
            for j in range(len(i)):
                if temp[j] == 1:
                    i[len(i)-j-1] = 0
                else:
                    i[len(i)-j-1] = 1
        
        return A