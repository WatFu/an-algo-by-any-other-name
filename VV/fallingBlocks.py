def fallingBlocks(matrix):
    #I: n x m grid 1 and 0's
    #O: array of tuples for coordinates(row, column)
    
    m = len(matrix)
    n = len(matrix[0])
    
    visited = {}
    
    curr_path = {}
    
    curr_lowest_row = {}
    
    res = []
    
    def dfs(node):
        s = node[0]
        t = node[1]
        if node not in visited and s > -1 and s < m and t > -1 and t < n and matrix[s][t] == 1:
            visited[(s,t)] = 1
            curr_path[(s, t)] = 1
            if t in curr_lowest_row:
                curr_lowest_row[t] = max(curr_lowest_row[t], s)
            else:
                curr_lowest_row[t] = s
            dfs((s + 1, t))
            dfs((s - 1, t))
            dfs((s, t + 1))
            dfs((s, t - 1))
    # flags = [False for _ in range(n)]
    for i in range(m - 2, -1, -1):
        for j in range(n):
            isValid = True
            if matrix[i][j] == 1 and (i, j) not in visited:
                dfs((i, j))
                for key in curr_lowest_row.keys():
                    if curr_lowest_row[key] >= m - 1:
                        isValid = False
                        break
                if isValid:
                    res += curr_path.keys()
                curr_path = {}
                curr_lowest_row = {}
            
    return res


    # for i in range(m - 2, -1, -1):
    #     stack = []
    #     isValid = True
    #     for j in range(n):
    #         if matrix[i][j] == 1:
    #             if matrix[i + 1][j] == 1:
    #                 isValid = False
    #             else:
    #                 stack.append((i, j))
    #         elif matrix[i][j] == 0:
    #             if isValid:
    #                 res += stack
    #                 for coord in stack:
    #                     matrix[coord[0]][coord[1]] = 0
    #             stack = []
    #             isValid = True
    #     if stack:
    #         res += stack
    #         # elif matrix[i][j] == 0:
    #         #     flags[j] = True
    # return res


# a = [[1,1,1,1], [0,0,1,0], [1,1,0,0], [0,0, 1,1]]
b = [[1,1,1,1,1],[0,0,1,0,1],[1,1,0,0,0]]
print(fallingBlocks(b))
