class Solution:
    def find(self, parent,i): 
        if parent[i] == -1: 
            return i 
        if parent[i]!= -1: 
            return self.find(parent,parent[i])
            
    def union(self,parent, edge, x,y): 
        x_set = self.find(parent, x) 
        y_set = self.find(parent, y) 
        
        if x_set == y_set:
            return
        
        if edge[x_set]:
            parent[y_set] = x_set
        else:
            parent[x_set] = y_set
        
        
    def solve(self, board: List[List[str]]) -> None:
        if not board:
			return
        w = len(board[0])
        h = len(board)
        
        if w <3 or h< 3 :
            return
        
        #initialize
        ds = []
        isOnEdge = []
        for i in range(h):
            for j in range(w):
                ds.append(-1)
                if i==0 or j==0 or i== h-1 or j==w-1:
                    isOnEdge.append(True)
                else:
                    isOnEdge.append(False)
                
                
        #setting ds
        
        for i in range(h):
            for j in range(w):
                if board[i][j]== 'O':
                    down = i +1
                    right = j+1
                    
                    if down < h:
                        if board[down][j] == 'O':
                            self.union(ds, isOnEdge, i*w+j, down*w+j)
                    
                    if right < w:
                        if board[i][right] == 'O':
                            self.union(ds, isOnEdge, i*w+j, i*w+right)
        
        for i in range(h):
            for j in range(w):
                if board[i][j]== 'O':
                    if not isOnEdge[self.find(ds, i*w+j)]:
                        board[i][j] = 'X'