R, C, K = map(int, input().split())
grid = [[0 for _ in range(C)] for _ in range(R+3)] # R - 2 offset (북쪽에서 시작 - 격자 밖)
gol_list = [tuple(map(int, input().split())) for _ in range(K)]
vis = [[0 for _ in range(C)] for _ in range(R+3)]
ans = []

def pr(arr=grid):
    for _ in range(len(arr)):
        print(*arr[_])
    print()

# 방향 : 북 동 남 서
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
EAST, SOUTH, WEST = 1, 2, 3


def is_empty(row, col, d):
    # 현재 좌표, 방향을 기반으로 전진 기준 좌표를 구합니다.
    nr, nc = row + dxs[d], col + dys[d]
    # 전진 기준 좌표에서 방향 기준으로 인접 두 방향 (총 세 방향)의 위치가 비어있는지 조사합니다.
    ld, rd = (d + 1)%4, (d -1)%4
    dir_list = [ld, d, rd]

    for dd in dir_list:
        nnr, nnc = nr + dxs[dd], nc + dys[dd]
        # 골렘이 존재하는 칸이 있다면

        if nnr >=R+3 or nnc < 0 or nnc >= C : # 바깥?
            return False

        if grid[nnr][nnc] > 0 :
            return False


    return True


def clear_grid():
    # global grid
    # grid = [[0 for _ in range(C)] for _ in range(R + 3)]  # R - 2 offset (북쪽에서 시작 - 격자 밖)
    for i in range(R+3):
        for j in range(C):
            grid[i][j] = 0

def clear_vis():
    # global vis
    # vis = [[0 for _ in range(C)] for _ in range(R + 3)]
    for i in range(R+3):
        for j in range(C):
            vis[i][j] = 0


def in_range(x, y):
    return 3<=x<R+3 and 0<=y<C


def bfs(row, col):
    from collections import deque
    q = deque()
    clear_vis()
    max_row = 0
    q.append((row, col))
    vis[row][col] = 1

    while q:
        x, y = q.popleft()
        # print(x, y)
        # 각 좌표에 따라서 상이하게 이동
        # 중심점이라면
        if grid[x][y] == 3 :
            for d in range(4):
                nx, ny = x +dxs[d], y + dys[d]
                if vis[nx][ny]: continue
                if not vis[nx][ny] and grid[nx][ny] == 2 :
                    vis[nx][ny] = 2
                    q.append((nx, ny))
                else :
                    vis[nx][ny] = 1

                max_row = max(nx, max_row)

        # 출구라면
        elif grid[x][y] == 2 :
            for d in range(4):
                nx, ny = x + dxs[d], y + dys[d]
                # 출구에서는 나갈 수 있음
                if not in_range(nx, ny): continue
                if vis[nx][ny]: continue
                if grid[nx][ny] > 0 :
                    vis[nx][ny] = 1
                    q.append((nx, ny))
                max_row = max(nx, max_row)

        else : # 곁가지
            for d in range(4):
                nx, ny = x + dxs[d], y + dys[d]
                # 출구에서는 나갈 수 있음
                if not in_range(nx, ny): continue
                if vis[nx][ny] : continue
                if grid[nx][ny] == 3 :
                    vis[nx][ny] = 3
                    q.append((nx, ny))
                # elif grid[nx][ny] > 0:
                #     vis[nx][ny] = grid[nx][ny]
                max_row = max(nx, max_row)

    # pr(vis)
    # print(max_row)
    return max_row - 2


for gol in gol_list : # K개의 골렘을 이동시킴
    # 시작 위치 초기화
    row = 1
    col, ex_dir = gol
    col -= 1 # offset

    # 종료조건
    while row <= R+1 :
        # 우선순위에 따른 검사
        # print(row, col, ex_dir)
        # 1. 아래로 전진 - 아래 좌표의 인접 세 지점을 검사 - 비어있으면 ?
        if is_empty(row, col, SOUTH):
            row += 1

        # 2. 서쪽으로 "반시계" 회전, 아래로 전진
        elif is_empty(row, col, WEST) and is_empty(row, col-1, SOUTH):
            row -= 1
            col -= 1
            ex_dir = (ex_dir-1)%4

        # 3. 동쪽으로 회전, 아래로 전진
        elif is_empty(row, col, EAST) and is_empty(row, col + 1, SOUTH):
            row -= 1
            col += 1
            ex_dir = (ex_dir + 1) % 4

        # 4. 불가능 시
        else :

            is_in_forest = True
            # 4-1. 빠져나간 부분이 존재한다면 ?
            for d in range(4):
                nr, nc = row + dxs[d], col + dys[d]
                if nr < 3 or nr >= R+3 or nc < 0 or nc >= C :
                    is_in_forest = False
                    break

            # 숲을 초기화 합니다.
            # 정령의 최종위치는 넣지 않습니다. (Break. not append)
            if not is_in_forest :
                clear_grid()
                break

            # 4-2. 모든 Body가 숲의 내부에 있다면 ?
            else :
                # 숲에 골렘을 안착(위치)
                grid[row][col] = 3 # Center
                vis[row][col] = 1

                for d in range(4):
                    nr, nc = row + dxs[d], col + dys[d]
                    if d == ex_dir :
                        grid[nr][nc] = 2
                    else :
                        grid[nr][nc] = 1

                # BFS를 통해 정령의 최종 위치를 도출 후 ans에 삽입합니다.
                ans.append(bfs(row, col))
                break

    # pr()
    # print(ans)

print(sum(ans))





