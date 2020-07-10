"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
# misunderstood problem, but interesting recursion tho i think maybe

        # p, next_flag = head, False
        # next_head = q = Node(None)
        # while p.next:
        #     if p.child != None:
        #         next_flag = True
        #         q.next = p.child
        #         next_head = self.flatten(next_head)
        #     elif not next_flag:
        #         q.next = Node(None)
        #     p = p.next
        # if next_flag:
        #     p.next = next_head
        # return head
        
# works for singly-linked
#         s = []
#         p = head
#         q = p.next
        
#         while q or s:
#             while not p.child and q:
#                 p = p.next
#                 q = q.next
#             if p and p.child:
#                 tmp = q
#                 p.next = p.child
#                 s.append(tmp)
#                 p = p.next
#                 q = p.next
#             if not q and s:
#                 tmp = s.pop()
#                 p.next = tmp
#                 p = tmp
#                 q = p.next
                
#         return head
        
        if not head:
            return None
    
        s = []
        p = head
        q = p.next
        
        while p or q or s:
            while p and q and not p.child:
                p = p.next
                q = q.next
            if p and p.child:
                tmp = q
                p.next = p.child
                p.child = None
                p.next.prev = p
                s.append(tmp)
                p = p.next
                q = p.next
            if not q and s:
                tmp = s.pop()
                if tmp != None:
                    p.next = tmp
                    tmp.prev = p
                    p = tmp
                    q = p.next
            if not q and not s and not p.child:
                break

        return head
# testing
#         p = head
#         while p:
#             if p.child:
#                 childval = p.child.val
#             else:
#                 childval = p.child
#             if p.next:
#                 nextval = p.next.val
#             else:
#                 nextval = p.next
#             if p.prev:
#                 prevval = p.prev.val
#             else:
#                 prevval = p.prev
#             print(p.val, childval, nextval, prevval)
#             p = p.next
            
