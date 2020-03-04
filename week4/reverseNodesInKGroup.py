# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        if head.next == None or k==1:
            return head
        
        n = head
        nprev = None
        
        firsta = None
        firstb = None
        
        
        while n!= None:
            i=0
            temp = n
            
            while i<k:
                if n==None:
                    if firstb==None:
                        return head
                    firstb.next = temp
                    return newHead
                
                newNode = ListNode(n.val)
                if i==0:
                    firstb = firsta
                    firsta = newNode
                newNode.next = nprev
                n = n.next
                nprev = newNode
                i+=1
                
            if firstb!=None:
                firstb.next = newNode
            firsta.next = None 
            
            if firstb ==None:
                newHead = newNode
        
        return newHead