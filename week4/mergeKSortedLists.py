# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappop, heappush, heapify

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        heap = []
        heapify(heap)
        
        for i in range(len(lists)):
            n = lists[i]
            while(n!=None):
                heappush(heap, n.val)
                n=n.next
                
        if not heap:
            return None
        
        res = ListNode(heappop(heap))
        n = res
        while len(heap)>0:
            n.next = ListNode(heappop(heap))
            n = n.next
        
        return res