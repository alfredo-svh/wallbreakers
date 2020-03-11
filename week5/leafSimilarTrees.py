# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(node, lvs):
            if node.left == None and node.right==None:
                lvs.append(node.val)
                return
            
            if node.left != None:
                helper(node.left, lvs)
            if node.right != None:
                helper(node.right, lvs)
            
        
        lvs1 = []
        lvs2 = []
                
        helper(root1, lvs1)
        helper(root2, lvs2)

        return lvs1 == lvs2