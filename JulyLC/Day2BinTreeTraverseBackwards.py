# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def levelTraverse(nodes, res=collections.deque([])):
            new_nodes = []
            curr_values = []
            for node in nodes:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
                curr_values.append(node.val)
            res.appendleft(curr_values)
            if not new_nodes:
                return res
            return levelTraverse(new_nodes, res)

        if not root:
            return []
        return levelTraverse([root])