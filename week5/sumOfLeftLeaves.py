# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def helper(n, f):
            if n.left==None and n.right==None:
                if f:
                    return n.val
                return 0
            
            l,r = 0,0
            
            if n.left != None:
                l = helper(n.left, True)
            if n.right != None:
                r = helper(n.right, False)
            
            return l + r
    
    
        if not root:
            return 0
        
        return helper(root,False)