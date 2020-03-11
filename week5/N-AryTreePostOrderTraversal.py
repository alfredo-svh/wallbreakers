"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        
        res = []
        n = [root]

        while True:
            
            while len(n[-1].children)>0:
                n.append(n[-1].children[0])
            
            res.append(n.pop().val)
            if len(n)==0:
                return res
            del n[-1].children[0]