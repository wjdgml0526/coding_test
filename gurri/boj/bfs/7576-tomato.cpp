#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

const int MX = 1002;
int board[MX][MX], dist[MX][MX];

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int N, M;

queue<pair<int, int>> Q;

bool inRange(int x, int y)
{
    return (0 <= x && x < N && 0 <= y && y < M);
}

void input()
{
    cin >> M >> N;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> board[i][j];

            if (board[i][j] == 0)
                dist[i][j] = -1;
            else if (board[i][j] == -1)
                dist[i][j] = 0;

            // 다 익은 토마토를 찾아서 큐에 넣기
            else
            {
                Q.push({i, j});
                dist[i][j] = 0;
            }
        }
    }
}

void bfs()
{
    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();
        int x = cur.X;
        int y = cur.Y;
        for (int dir = 0; dir < 4; dir++)
        {
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            // 범위 밖
            if (!inRange(nx, ny))
                continue;
            // 이미 방문? 혹은 벽?
            if (dist[nx][ny] >= 0 || board[nx][ny] == -1)
                continue;
            dist[nx][ny] = dist[x][y] + 1;
            Q.push({nx, ny});
        }
    }
}

void printAnswer()
{
    int minDate = 0;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (dist[i][j] == -1)
            {
                cout << -1 << '\n';
                return;
            }

            minDate = max(minDate, dist[i][j]);
        }
    }
    cout << minDate << '\n';
}

int main(void)
{

    input();
    // BFS
    bfs();
    // 다 익는 최소 날짜를 출력
    // for (int i = 0; i < N; i++)
    // {
    //     for (int j = 0; j < M; j++)
    //         cout << dist[i][j] << ' ';
    //     cout << '\n';
    // }

    printAnswer();
    // 다 익지않았으면, -1을 반환
}