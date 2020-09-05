import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.els = []
        heapq.heapify(self.els)
        self.addToHeap(root1)
        self.addToHeap(root2)
        res = []
        n = len(self.els)
        for i in range(n):
            res.append(heapq.heappop(self.els))
        return res
        
    def addToHeap(self, node):
        if node == None:
            return
        heapq.heappush(self.els, node.val)
        self.addToHeap(node.left)
        self.addToHeap(node.right)
