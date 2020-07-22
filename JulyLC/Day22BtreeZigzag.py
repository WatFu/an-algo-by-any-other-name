# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        def traverseHelper(nodes, flag):
            curr_nodes = []
            next_nodes = []
            
            for node in nodes:
                curr_nodes.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            
            if flag:
                curr_nodes.reverse()
            res.append(curr_nodes)
            
            if next_nodes:
                traverseHelper(next_nodes, not flag)
        
        
        traverseHelper([root], False)
        return res
