class Node:
    def __init__(self):
        self.isEnding = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        nd = self.root
        
        for i in range(len(word)):
            if word[i] not in nd.children:
                nd.children[word[i]] = Node()

            nd = nd.children[word[i]]
            
        nd.isEnding = True

    def search(self) -> str:
        def helper(nd, cur):
            res = cur
            mx = len(res)
            for k,v in nd.children.items():
                if not v.isEnding:
                    continue
                tmp = helper(v, cur+k)
                if (len(tmp) > mx) or (len(tmp)==mx and tmp<res):
                    res = tmp
                    mx = len(tmp)
            
            return res
        
        nod = self.root
        return helper(nod, "")
    
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        t = Trie()
        
        for i in words:
            t.insert(i)
            
        
        return t.search()