# INPUT
K, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(5)]
fill_nums = list(map(int, input().split()))
ptr = 0
vis = [[0 for _ in range(5)] for _ in range(5)]
temp = [[0 for _ in range(5)] for _ in range(5)]
origin = [[None for _ in range(5)] for _ in range(5)]
bucket = []


# temp에 복사를 하고, 방문 처리 초기화를 진행
def copy_grid():
    for i in range(5):
        for j in range(5):
            temp[i][j] = grid[i][j]


def pr(arr=grid):
    for _ in range(len(arr)):
        print(*arr[_])
    print()


def rotate(r, c, rot):
    # (r, c)를 기준으로 3x3의 행렬을 선택
    tmp_mat = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            tmp_mat[i - r][j - c] = temp[i][j]

    # temp행렬에 회전 및 복사를 진행
    # temp에 회전 결과를 대입
    if rot == 1:  # 90
        for i in range(3):
            for j in range(3):
                temp[i + r][j + c] = tmp_mat[3 - 1 - j][i]
    elif rot == 2:  # 180
        for i in range(3):
            for j in range(3):
                temp[i + r][j + c] = tmp_mat[3 - 1 - i][3 - 1 - j]
    else:  # 270
        for i in range(3):
            for j in range(3):
                temp[i + r][j + c] = tmp_mat[j][3 - 1 - i]


def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def bfs():
    # temp에 대해 bfs를 진행하여, 가치 값을 계산 및 반환
    global bucket
    bucket = []
    from collections import deque
    q = deque()
    val = 0
    for i in range(5):
        for j in range(5):
            vis[i][j] = 0
            origin[i][j] = None

    for i in range(5):
        for j in range(5):
            if not vis[i][j]:
                temp_bucket = []
                cnt = 1
                q.append((i, j))
                vis[i][j] = 1
                # temp에 대해 bfs를 진행합니다.
                while q:
                    x, y = q.popleft()
                    for dx, dy in zip(dxs, dys):
                        nx, ny = x + dx, y + dy
                        if not in_range(nx, ny): continue
                        if temp[x][y] == temp[nx][ny] and not vis[nx][ny]:
                            cnt += 1
                            vis[nx][ny] = 1
                            q.append((nx, ny))

                            temp_bucket.append((nx, ny))
                            # 이렇게 하면, cnt <3의 경우도 담기게 되는 문제

                if cnt >= 3:
                    bucket.append((i, j))
                    bucket.extend(temp_bucket)
                    val += cnt
    return val


def find_maxvalue():
    # 탐사를 진행합니다.
    # 우선순위 - 각도, 중심좌표 열(y), 행(c)가 작은 순으로 진행
    maxi = 0
    max_r, max_c, max_rot = -1, -1, -1
    # 3 x 3의 격자를 선택합니다.
    # 회전을 진행합니다.
    # 열 순으로 순회 # 행 순으로 순회
    for rot in range(1, 4):  # rot = 1, 2, 3
        for c in range(5 - 3 + 1):
            for r in range(5 - 3 + 1):
                copy_grid()  # temp 에 복사
                rotate(r, c, rot)  # 선택된 격자의 회전 결과를 TEMP에 입력
                val = bfs()
                if val > maxi:
                    maxi = val
                    max_r, max_c, max_rot = r, c, rot

    return maxi, max_r, max_c, max_rot


# K번 탐사를 반복합니다.
for _ in range(K):
    value = 0
    ret, r, c, rot = find_maxvalue()

    if ret == 0:
        break
    # 초기가치를 획득합니다.
    copy_grid()  # temp 에 복사
    rotate(r, c, rot)
    # 연쇄반응
    # cond : 획득 가치 3미만 일 경우 Stop
    val = bfs()
    st = []
    st.append(val)
    # 연쇄가치를 획득합니다.
    while st:
        val = st.pop()

        if val == 0:
            break
        value += val

        # 획득하게 된 유물조각을 새로 채웁니다.
        bucket.sort(key=lambda x: (x[1], -x[0]))  # 열 작은, 행 큰 순으로 채우기 위한 정렬
        for (r, c) in bucket:
            temp[r][c] = fill_nums[ptr]
            ptr += 1

        val = bfs()
        # print(val)
        st.append(val)
    # pr(temp)
    # 격자판을 갱신합니다.
    for i in range(5):
        for j in range(5):
            grid[i][j] = temp[i][j]

    print(value, end=" ")