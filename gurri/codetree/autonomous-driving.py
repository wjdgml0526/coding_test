n, m = map(int, input().split())
x, y, d = map(int, input().split())
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
grid = [list(map(int, input().split())) for _ in range(n)]
vis = [[0 for _ in range(m)] for _ in range(n)]

vis[x][y] = 1
turn = 0

while True :
    nd = (d - 1) % 4
    nx, ny = x + dx[nd], y + dy[nd]

    # 왼쪽 방향을 한번 도 간적이 없다면 
    if not vis[nx][ny] and grid[nx][ny] != 1 : 
        # 좌회전 및 전진
        vis[nx][ny] = 1
        x, y, d = nx, ny, nd
        turn = 0
        
    else : # 인도/ 간적 있다면 ? 좌회전 반복
        if turn != 4 : # 4방향 탐색
            d = nd
            turn += 1
        # 방향 유지 및 한칸 후진 후 1반복    
        else : 
            d^= 2 # 반대방향
            nx, ny = x + dx[d], y + dy[d]
            if grid[nx][ny] != 1 : 
                x, y = nx, ny
                d ^= 2
                turn = 0
            
            else:
                break


ans = sum(
    vis[x][y]
    for x in range(n)
    for y in range(m)
    if vis[x][y]
)
print(ans)

