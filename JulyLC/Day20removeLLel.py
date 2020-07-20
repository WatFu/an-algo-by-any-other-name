# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        newhead = p = ListNode(0)
        q = head
        
        while q:
            p.next = None
            if q.val == val:
                q = q.next
            else:
                p.next = q
                p = q
                q = q.next
        
        return newhead.next
