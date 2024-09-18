from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh += 1

        dxs, dys = [0,1,0,-1],[1,0,-1,0]
        max_time = 0

        while queue:
            x, y, time = queue.popleft()
            for dx, dy in zip(dxs,dys):
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh -= 1
                    queue.append((nx, ny, time+1))
                    max_time = max(max_time, time+1)
        if fresh >0:
            return -1
        return max_time