# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        
        if head.next == None or m==n:
            return head
        
        current = head
        before = None
        
        # get:
        # -before: node before m
        # -last = m-th node
        i=1
        while i < m:
            before = current
            current = current.next
            i+=1
            
        nprev = ListNode(current.val)
        last = nprev
        
        
        #reverse until n
        while i < n:
            
            newNode = ListNode(current.next.val)
            newNode.next = nprev
            current = current.next
            nprev = newNode
            i+=1
        
        #link it back to the original
        last.next = current.next
        if m!=1:
            before.next = newNode
        else:
            return newNode
        
        return head