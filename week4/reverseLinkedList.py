# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        n= head.next
        nprev = ListNode(head.val)
        
        while(n!=None):
            
            newNode = ListNode(n.val)
            newNode.next = nprev
            n = n.next
            nprev = newNode
        
        return nprev