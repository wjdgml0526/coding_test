class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

        visited = [
            [0 for _ in range(cols)] for _ in range(rows)
        ]

        cnt = 0
        # bfs - queue
        q = deque()

        def in_range(x, y):
            return 0 <= x < rows and 0 <= y < cols

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c] == "1":

                    q.append((r, c))
                    visited[r][c] = 1

                    while q:
                        x, y = q.popleft()
                        for i in range(4):
                            nx, ny = x + dxs[i], y + dys[i]

                            if in_range(nx, ny) and not visited[nx][ny] \
                                    and grid[nx][ny] == "1":
                                visited[nx][ny] = 1
                                q.append((nx, ny))

                    # end of bfs
                    cnt += 1


        return cnt
