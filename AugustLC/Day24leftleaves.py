# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.travHelper(root, 0)
    
    def travHelper(self, node, isLeft):
        res = 0
        if not node:
            return 0
        if not node.left and not node.right and isLeft:
            res += node.val
        res = res + self.travHelper(node.left, 1) + self.travHelper(node.right, 0)
        return res
        
