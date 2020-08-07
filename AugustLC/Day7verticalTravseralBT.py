import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        h = collections.defaultdict(list)

        lowest = [0]
        res = []
        
        def bfs(nodes):
            next_nodes = []
            curr_vals = collections.defaultdict(list)
            for node in nodes:
                curr_vals[node[0]].append(node[1].val)
                    
                # if node[0] in h:
                #     h[node[0]].append(node[1].val)
                # else:
                #     h[node[0]] = [node[1].val]
                if node[1].left:
                    if node[0] - 1 < lowest[0]:
                        lowest[0] = node[0] - 1
                    next_nodes.append([node[0] - 1, node[1].left])
                if node[1].right:
                    next_nodes.append([node[0] + 1, node[1].right])
            for key in list(curr_vals.keys()):
                h[key] += sorted(list(curr_vals[key]))
            if not next_nodes:
                return
            bfs(next_nodes)
        
        bfs([[0, root]])
        
        while True:

            if not lowest[0] in h:
                break

            res.append(list(h[lowest[0]]))
            lowest[0] += 1
        
        return res
                
