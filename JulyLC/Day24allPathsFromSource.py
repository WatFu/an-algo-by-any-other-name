class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        
        res = []
        
        def dfs(node, curr_stack):
            curr_stack.append(node)
            if node == end:
                tmp = curr_stack.copy()
                res.append(tmp)
                return
            for next_node in graph[node]:
                dfs(next_node, curr_stack)
                curr_stack.pop()
        
        dfs(0, [])
        
        return res
