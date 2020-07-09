# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        def calcWidth(arr):
            l_pointer, r_pointer = 0, len(arr) - 1
            
            while arr[l_pointer] == None:
                l_pointer += 1
                if l_pointer > r_pointer:
                    return 0, 0, 0
            while arr[r_pointer] == None:
                r_pointer -=1
            
            return r_pointer - l_pointer + 1, l_pointer, r_pointer
        
        def bfsTraverse(nodes, max_width):
            new_nodes = []
            for node in nodes:
                if node != None:
                    new_nodes.append(node.left)
                    new_nodes.append(node.right)
                else:
                    new_nodes.append(None)
                    new_nodes.append(None)
            
            new_width, l_slice, r_slice = calcWidth(new_nodes)
            if new_width > max_width:
                max_width = new_width
            if new_width == 0:
                return max_width
            return bfsTraverse(new_nodes[l_slice: r_slice + 1], max_width)
        
        if not root:
            return 0
        return bfsTraverse([root], 1)
            
