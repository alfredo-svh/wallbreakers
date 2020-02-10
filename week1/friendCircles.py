class Solution:
    def find(self, parent,i): 
        if parent[i] == -1: 
            return i 
        if parent[i]!= -1: 
             return self.find(parent,parent[i])
            
    def findCircleNum(self, M: List[List[int]]) -> int:
        people = len(M)
        circles = len(M)
        
        friend = [-1]*people
        
        for i in range(people):
            for j in range(i+1, people):
                if M[i][j] == 1:
                    x = self.find(friend, i)
                    y = self.find(friend, j)                   
                    if x!=y:
                        friend[x] = y
                        circles-=1
                        
        return circles