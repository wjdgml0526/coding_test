from collections import deque

class Solution:
    def pacificAtlantic(self, M):
        
        n, m = len(M), len(M[0])

        def bfs(starts):
            q = deque(starts)
            visit = [[0 for _ in range(m)] for _ in range(n)]
            visited = set(starts)
            
            dxs, dys = [0,1,0,-1], [1,0,-1,0]

            while q : 
                x, y = q.popleft()

                if (x, y) in visited:
                    continue

                for dx, dy in zip(dxs,dys):
                    nx, ny = x+dx, y+dy

                    if 0<=nx<n and 0<=ny<m and (nx, ny) not in visited :
                        if M[x][y] <= M[nx][ny]:
                            q.append((nx, ny))
                            visited.add((nx, ny))

            return visited            

        
        pacific = [(0, i) for i in range(m)] + [(i, 0) for i in range(n)]
        atlantic = [(n-1, i) for i in range(m)] + [(i, m-1) for i in range(n)]

        return bfs(atlantic) & bfs(pacific)