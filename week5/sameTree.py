# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def helper(p,q):
            #not the same value
            if p.val != q.val:
                return False
            
            #not the same children
            if p.left==None and q.left!=None or p.left!=None and q.left==None or p.right==None and q.right!=None or p.right!=None and q.right==None:
                return False
            
            #both are leaves
            if p.left==None and p.right==None:
                return True
            
            l,r = True, True
            
            if p.left != None:
                l = helper(p.left, q.left)
            if p.right != None:
                r = helper(p.right, q.right)
            
            return l and r
        
        
        if not p or not q:
            return not p and not q
        
        return helper(p,q)