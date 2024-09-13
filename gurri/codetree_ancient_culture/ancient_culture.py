from collections import deque

N_large = 5
N_small = 3

class Board:
    def __init__(self):
        self.a = [[0 for _ in range(N_large)] for _ in range(N_large)]
    
    def in_range(self, y, x):
        return 0<=y < N_large and 0<= x <N_large

    def rotate(self, sy, sx, cnt):
        # 내부에 클래스 인스턴스를 ?
        result = Board()
        result.a = [row[:] for row in self.a]
        for _ in range(cnt):
            # sy, sx를 좌 상단으로 시계 방향 90도 회정
            tmp = result.a[sy + 0][sx + 2]
            result.a[sy + 0][sx + 2] = result.a[sy + 0][sx + 0]                
            result.a[sy + 0][sx + 0] = result.a[sy + 2][sx + 0]                                
            result.a[sy + 2][sx + 0] = result.a[sy + 2][sx + 2]                                
            result.a[sy + 2][sx + 2] = tmp
            tmp = result.a[sy + 1][sx + 2]
            result.a[sy + 1][sx + 2] = result.a[sy + 0][sx + 1]                
            result.a[sy + 0][sx + 1] = result.a[sy + 1][sx + 0]                                
            result.a[sy + 1][sx + 0] = result.a[sy + 2][sx + 1]                                
            result.a[sy + 2][sx + 1] = tmp                                                
        return result

    def cal_score(self):
        score = 0
        visit = [
            [False for _ in range(N_large)] for _ in range(N_large)
        ]
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

        for i in range(N_large):
            for j in range(N_large):
                if not visit[i][j]:
                    # BFS를 활용한
                    # Flood fill 알고리즘을 사용해서 visit 배열 채운다.
                    # trace 에 조각들 위치가 저장
                    q, trace = deque([(i, j)]), deque([(i, j)])
                    visit[i][j] = True
                    while q:
                        cur = q.popleft()
                        for k in range(4):
                            ny, nx = cur[0] + dy[k], cur[1] + dx[k]
                            if self.in_range(ny, nx) and \
                            self.a[ny][nx] == self.a[cur[0]][cur[1]] and \
                            not visit[ny][nx]:
                                q.append((ny, nx))
                                # Flood fill
                                trace.append((ny, nx))
                                visit[ny][nx] = True 
                    # flood fill을 통해 조각들이 모여 유물이 되고 사라지는 지 확인
                    if len(trace) >= 3:
                        # 유물이 되어 사라지느 경우 가치를 더해주고 조각이 비어 있음을 뜻하는 0으로 대치합니다.
                        score += len(trace)
                        while trace:
                            t = trace.popleft()
                            self.a[t[0]][t[1]] = 0
        return score
    
    # 유물 획득 과정에서 조각 비어있는 곳에 새로 조각 채웁니다.
    def fill(self, que):
        # 열이 작고, 행이 큰 순으로 채운다
        for j in range(N_large):
            for i in reversed(range(N_large)): # 행이 큰! - reversed
                if self.a[i][j] == 0:
                    self.a[i][j] = que.popleft()

def main():
    # 입력받기
    K, M = map(int, input().split())
    board = Board()
    for i in range(N_large):
        board.a[i] = list(map(int, input().split())) # 한번에 대치
    q = deque()
    for t in list(map(int, input().split())):
        q.append(t)
    
    for _ in range(K):
    # 최대 K번의 탐사를 진행
        maxScore = 0
        maxScoreBoard = None

        # 우선순위 - 유물의 1차획득 가치 / 회전 각도 / 열 / 행 작은 순
        for cnt in range(1, 4):
            for sx in range(N_large - N_small + 1):
                for sy in range(N_large - N_small + 1):
                    rotated = board.rotate(sy, sx, cnt)
                    score = rotated.cal_score()

                    if maxScore < score:
                        maxScore = score
                        maxScoreBoard = rotated
    
        # 회전 통해 더 이상 유물 획득 불가 시 종료
        if maxScoreBoard is None:
            break
        board = maxScoreBoard
        
        # 유물의 연쇄획득 진행
        while True :
            board.fill(q)
            newScore = board.cal_score()
            if newScore == 0:
                break
            maxScore += newScore
        print(maxScore, end =" ")

if __name__ == "__main__":
    main()