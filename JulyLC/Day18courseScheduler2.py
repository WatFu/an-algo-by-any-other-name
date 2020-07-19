import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = {}
        current_loop = {}
        pre = collections.defaultdict(list)
        res = []
        flag = [False]
        
        for edge in prerequisites:
            pre[edge[1]].append(edge[0])
        
        def dfs(node):
            visited[node] = True
            current_loop[node] = True
            
            for next_node in pre[node]:
                if next_node in current_loop:
                    flag[0] = True
                    return
                if not next_node in visited:
                    dfs(next_node)
            
            del current_loop[node]
            res.append(node)
        
        for i in range(numCourses):
            if not i in visited:
                dfs(i)
        
        if flag[0]:
            return []
        res.reverse()
        return res
