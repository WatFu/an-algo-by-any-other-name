class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = {}
        m, n = len(grid), len(grid[0])
        
        def is_valid(square):
            if square[0] < 0 or square[0] > m - 1 or square[1] < 0 or square[1] > n - 1:
                return 0
            return 1
        
        def bfs(curr_square, count):
            visited[(curr_square[0],curr_square[1])] = 1
            
            up = (curr_square[0] - 1, curr_square[1])
            down = (curr_square[0] + 1, curr_square[1])
            right = (curr_square[0], curr_square[1] + 1)
            left = (curr_square[0], curr_square[1] - 1)
            
            curr_count = count
            
            if is_valid(up) and grid[up[0]][up[1]]:
                if not up in visited:
                    count += bfs(up, curr_count)
            else:
                count += 1
            if is_valid(down) and grid[down[0]][down[1]]:
                if not down in visited:
                    count += bfs(down, curr_count)
            else:
                count += 1
            if is_valid(right) and grid[right[0]][right[1]]:
                if not right in visited:
                    count += bfs(right, curr_count)
            else:
                count += 1
            if is_valid(left) and grid[left[0]][left[1]]:
                if not left in visited:
                    count += bfs(left, curr_count)
            else:
                count += 1
            return count
        
        start_square = (-1, -1)
        #find first piece of land, maybe suboptimal
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_square = (i,j)
                    break
            if start_square != (-1, -1):
                break
        
        if start_square == (-1, -1):
            return 0
        
        return bfs(start_square, 0)
