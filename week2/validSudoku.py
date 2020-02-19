class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        blocks = [set() for i in range(9)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                
                #rows
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])
                    
                #columns
                if board[i][j] in columns[j]:
                    return False
                else:
                    columns[j].add(board[i][j])
                
                #blocks
                bl = (j//3) + (i - i%3)
                if board[i][j] in blocks[bl]:
                    return False
                else:
                    blocks[bl].add(board[i][j])
                    
        return True