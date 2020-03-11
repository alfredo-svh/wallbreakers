# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def helper(n, i, mx, f):

            if n.left==None and n.right==None:
                if i>mx and f:
                    return (i, n.val)
                return (mx,0)
            
            l,r = 0,0
            
            if n.left != None:
                mx, l = helper(n.left,i+1, mx, True)
            if n.right != None:
                mx, r = helper(n.right, i+1, mx, n.left==None)
            
            if r !=0:
                return (mx, r)
            return (mx, l)
    
        
        i, res = helper(root,1, 0,True)
        return res