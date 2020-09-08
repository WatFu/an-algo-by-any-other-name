# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.total = 0
        
        if not root:
            return 0
        
        self.sumHelper(root, '')
        
        return self.total
        
    def sumHelper(self, node, curr):
        curr += str(node.val)
        if not node.right and not node.left:
            self.total += int(curr, 2)
            return
        if node.right:
            self.sumHelper(node.right, curr)
        if node.left:
            self.sumHelper(node.left, curr)
