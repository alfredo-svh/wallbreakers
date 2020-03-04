# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if not head:
            return 
        if head.next == None:
            return head
        
        
        fEven = ListNode(head.next.val)
        curEven = fEven
        lOdd = head
        
        i=2
        n =lOdd.next
        nprev = lOdd
        
        while n != None:
            if i%2==0:
                nprev.next = n.next
                if i!=2:
                    curEven.next = n
                    curEven = n
                    
            else:
                lOdd = n
            
            
            nprev = n
            n=n.next
            i+=1
        
        lOdd.next = fEven
        curEven.next = None
        
        return head