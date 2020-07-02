# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def levelTraverse(nodes, res=[]):
            new_nodes = []
            curr_values = []
            for node in nodes:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
                curr_values.append(node.val)
            res.append(curr_values)
            if not new_nodes:
                return res[::-1]
            return levelTraverse(new_nodes, res)

        if not root:
            return []
        return levelTraverse([root])