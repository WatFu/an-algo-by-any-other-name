class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        self.minutes = 0
        self.one = 0
        two_arr = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.one += 1
                elif grid[i][j] == 2:
                    two_arr.append((i, j))
        
        if not grid or self.one == 0:
            return 0
        
        def isValid(s, t):
            return s > -1 and s < m and t > -1 and t < n
        
        def bfs(nodes):
            next_nodes = []
            for node in nodes:
                y = node[0]
                x = node[1]
                if isValid(y - 1, x) and grid[y - 1][x] == 1:
                    self.one -= 1
                    grid[y - 1][x] = 0
                    next_nodes.append((y - 1, x))
                if isValid(y + 1, x) and grid[y + 1][x] == 1:
                    self.one -= 1
                    grid[y + 1][x] = 0
                    next_nodes.append((y + 1, x))
                if isValid(y, x - 1) and grid[y][x - 1] == 1:
                    self.one -= 1
                    grid[y][x - 1] = 0
                    next_nodes.append((y, x - 1))
                if isValid(y, x + 1) and grid[y][x + 1] == 1:
                    self.one -= 1
                    grid[y][x + 1] = 0
                    next_nodes.append((y, x + 1))
            self.minutes += 1
            if self.one == 0 or not next_nodes:
                return
            bfs(next_nodes)
        
        bfs(two_arr)
        
        if self.one != 0:
            return -1
        
        return self.minutes
