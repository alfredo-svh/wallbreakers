class Node:
    def __init__(self):
        self.word = ""
        self.children = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        nd = self.root

        for i in range(len(word)):
            if word[i] not in nd.children:
                nd.children[word[i]] = Node()

            nd = nd.children[word[i]]

        nd.word = word

class Solution:
    def search(self,board, n, i,j,res):
        c = board[i][j]
        if c == "*" or c not in n.children:
            return
        
        n = n.children[c]
        
        if n.word != "":
            res.append(n.word)
            n.word = ""
            
        board[i][j] = "*"
        #up
        if i > 0:
            self.search(board, n, i-1, j, res)
        #down
        if i < len(board)-1:
            self.search(board, n, i+1, j, res)
        #right
        if j < len(board[0])-1:
            self.search(board, n, i, j+1, res)
        #left
        if j>0:
            self.search(board, n, i, j-1, res)
            
        board[i][j] = c
        
        

        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        t = Trie()
        res = []
        
        #populate trie
        for word in words:
            t.insert(word)
            
        #search words in board
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(board, t.root, i, j, res)

        return res