# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        res = [0]
        
        def bfs(nodes):
            next_nodes = []
            for node in nodes:
                if node[1].val == sum:
                     res[0] += 1
                curr_sums = node[0]
                nextleft_sums = []
                nextright_sums = []
                if node[1].left:
                    nextleft_sums.append(node[1].left.val)
                    for val in curr_sums:
                        next_left = val + node[1].left.val
                        nextleft_sums.append(next_left)
                        if next_left == sum:
                            res[0] += 1
                    next_nodes.append([nextleft_sums, node[1].left])
                if node[1].right:
                    nextright_sums.append(node[1].right.val)
                    for val in curr_sums:
                        next_right = val + node[1].right.val
                        nextright_sums.append(next_right)
                        if next_right == sum:
                            res[0] += 1
                    next_nodes.append([nextright_sums, node[1].right])
            if not next_nodes:
                return
            bfs(next_nodes)
        
        bfs([[[root.val], root]])
            
        return res[0]
