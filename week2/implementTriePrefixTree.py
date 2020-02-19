class Node:
    def __init__(self):
        self.isEnding = False
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
            
        nd.isEnding = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        nd = self.root
        
        for i in range(len(word)):
            
            if word[i] not in nd.children:
                return False
            
            nd = nd.children[word[i]]
            
        return nd.isEnding
                
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        nd = self.root
        
        for i in range(len(prefix)):
            
            if prefix[i] not in nd.children:
                return False
            
            nd = nd.children[prefix[i]]
            
        return True