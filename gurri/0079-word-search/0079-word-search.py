from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Backtracking + DFS
        m, n = len(board), len(board[0])        
        
        def dfs(x, y, k):
            # 기저조건
            if k == len(word):
                return True
            # 범위 밖이거나, 아니라면
            if x < 0 or x >=m or y < 0 or y >=n or word[k] != board[x][y]:
                return False
            
            visited = board[x][y]
            board[x][y] = '.'

            board[x][y] = visited # dfs
            return result


        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False

        # m, n = len(board), len(board[0])        
        # visited = [[0 for _ in range(n)] for _ in range(m)]
        # def pr(arr):
        #     for _ in range(len(arr)):
        #         print(*arr[_])

        # q = deque()
        # # word를 만들 수 있는지 ? 
        # def bfs(x, y):

        #     q.append((x, y))
        #     visited[x][y] = 1
        #     idx = 1

        #     if idx == len(word):
        #         return True

        #     def in_range(x, y):
        #         return 0<=x<m and 0<=y<n
            
        #     # 초기화 된 격자에서 dfs를 시작 - word를 따라 갈 수 있어야 함.
        #     dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
            

        #     while q:
        #         x, y = q.pop()
        #         print(x, y)

        #         for dx, dy in zip(dxs, dys):
        #             nx, ny = x + dx, y + dy
        #             # 조건 검사
        #             if not in_range(nx, ny): continue
        #             if visited[nx][ny] : continue

        #             # 각 알파벳 별 방문처리가... 77/87

        #             if board[nx][ny] == word[idx]:
        #                 visited[nx][ny] = 1
        #                 print(word[idx])
        #                 q.append((nx, ny))    
        #                 idx += 1 

        #             if idx == len(word):
        #                 return True
            
        #     return False
                
        # # board에서 bfs를 진행 해서, word를 만들 수 있는지?
        # # 초기화 - word[0]이 grid내에 있는지 탐색 후 시작
        # for x in range(m):
        #     for y in range(n):
        #         if board[x][y] == word[0]:
        #             # visited 초기화
        #             visited = [[0 for _ in range(n)] for _ in range(m)]
                    
        #             if bfs(x, y): 
        #                 return True
        
        # return False