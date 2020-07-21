class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        if m == 0 or n == 0:
            return false
        flag = [False]
        curr_stack = {}
        
        def isValid(j, i):
            return i > -1 and j > -1 and i < n and j < m
        
        def dfs(char, y, x, curr_stack):
            if char == len(word):
                flag[0] = True
                return
            if flag[0] == False and isValid(y, x) and board[y][x] == word[char] and not (y, x) in curr_stack:
                curr_stack[(y,x)] = 1
                dfs(char + 1, y + 1, x, curr_stack)
                dfs(char + 1, y - 1, x, curr_stack)
                dfs(char + 1, y, x + 1, curr_stack)
                dfs(char + 1, y, x - 1, curr_stack)
                
                del curr_stack[(y,x)]
                
            return
        
        for j in range(m):
            for i in range(n):
                if board[j][i] == word[0]:
                    dfs(0, j, i, {})
                    if flag[0] == True:
                        return True
        
        return False
        
        
                
                
        # BFS is TLE
#         m = len(board)
#         n = len(board[0])
#         flag = [False]
        
#         def isValid(j, i):
#             return i > -1 and j > -1 and i < n and j < m
        
#         def bfs(char, y, x, curr_stack):
#             # print(char, curr_stack, x, y, board[y][x])
#             if char == len(word):
#                 flag[0] = True
#                 return
#             curr_letter = word[char]
            
#             if isValid(y + 1, x) and not (y + 1, x) in curr_stack and board[y + 1][x] == curr_letter:
#                 curr_stack[(y+1,x)] = 1
#                 bfs(char + 1, y + 1, x, curr_stack)
#                 del curr_stack[(y+1,x)]
#             if isValid(y - 1, x) and not (y - 1, x) in curr_stack and board[y - 1][x] == curr_letter:
#                 curr_stack[(y - 1,x)] = 1
#                 bfs(char + 1, y - 1, x, curr_stack)
#                 del curr_stack[(y-1,x)]
#             if isValid(y, x + 1) and not (y, x + 1) in curr_stack and board[y][x + 1] == curr_letter:
#                 curr_stack[(y, x + 1)] = 1
#                 bfs(char + 1, y, x + 1, curr_stack)
#                 del curr_stack[(y,x + 1)]
#             if isValid(y, x - 1) and not (y, x - 1) in curr_stack and board[y][x - 1] == curr_letter:
#                 curr_stack[(y, x - 1)] = 1
#                 bfs(char + 1, y, x - 1, curr_stack)
#                 del curr_stack[(y,x - 1)]
#             # print('here', y, x, curr_stack, board[y][x])
                
#         for j in range(m):
#             for i in range(n):
#                 if board[j][i] == word[0]:
#                     bfs(1, j, i, {(j, i): 1})
        
#         return flag[0]
