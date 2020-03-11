class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def helper(i, j, visited):
            
            # if current cell is water, add 1 to perimeter
            if i<0 or j<0 or i==len(grid) or j==len(grid[0]) or grid[i][j]== 0:
                return 1
            
            if visited[i][j]:
                return 0
            
            visited[i][j] = True
            
            per = 0
            
            #DFS
            per += helper(i-1,j, visited)
            per += helper(i,j-1, visited)
            per += helper(i+1,j, visited)
            per += helper(i,j+1, visited)
            
            return per
        

        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        
        #find island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return helper(i,j, visited)