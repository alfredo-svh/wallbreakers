# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        nodeA = headA
        nodeB = headB
        lastA = None
        lastB = None
        
        while(nodeA!= nodeB):
            if nodeA.next!=None:
                nodeA = nodeA.next
            else:
                lastA = nodeA
                nodeA=headB
            
            if nodeB.next!=None:
                nodeB = nodeB.next
            else:
                lastB = nodeB
                nodeB=headA
            
            if lastA!=None and lastB!=None:
                if lastA!=lastB:
                    return None
        
        return nodeA