class Solution:
    def find_parent(self, parent,i): 
        if parent[i] == -1: 
            return i 
        if parent[i]!= -1: 
             return self.find_parent(parent,parent[i]) 
            
    def union(self,parent,x,y): 
        x_set = self.find_parent(parent, x) 
        y_set = self.find_parent(parent, y) 
        
        if x_set != y_set:
            parent[x_set] = y_set 
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        h = len(grid)
        w = len(grid[0])
        ds = [-1]*(w*h)
        count = 0
        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    if i-1>=0:
                        if(grid[i-1][j]=="1"):
                            self.union(ds, i*w+j, (i-1)*w+j)
                    if i+1<h:
                        if(grid[i+1][j]=="1"):
                            self.union(ds, i*w+j, (i+1)*w+j)
                    if j-1>=0:
                        if(grid[i][j-1]=="1"):
                            self.union(ds, i*w+j, i*w+j-1)
                    if j+1<w:
                        if(grid[i][j+1]=="1"):
                            self.union(ds, i*w+j, i*w+j+1)
                    
        for i in range(h):
            for j in range(w):
                if grid[i][j]== "1" and ds[i*w+j]==-1:
                    count+=1
        
        return count