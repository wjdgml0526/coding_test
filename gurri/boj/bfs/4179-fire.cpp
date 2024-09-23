#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

const int MX = 1002;

string grid[MX];
int dist[MX][MX], fire[MX][MX];
int R, C;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

queue<pair<int, int>> Q1;
queue<pair<int, int>> Q2;

void pr(int g[MX][MX])
{
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
            cout << g[i][j] << ' ';
        cout << '\n';
    }
}

int main(void)
{
    // 입력
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> R >> C;
    for (int i = 0; i < R; i++)
    {
        fill(dist[i], dist[i] + C, -1);
        fill(fire[i], fire[i] + C, -1);
    }

    for (int i = 0; i < R; i++)
        cin >> grid[i];

    // 초기화
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            // 지훈이
            if (grid[i][j] == 'J')
            {
                Q1.push({i, j});
                dist[i][j] = 0;
            }

            // 불
            if (grid[i][j] == 'F')
            {
                Q2.push({i, j});
                fire[i][j] = 0;
            }
        }
    }

    // 불의 영역 전개 - BFS
    while (!Q2.empty())
    {
        auto cur = Q2.front();
        Q2.pop();
        for (int dir = 0; dir < 4; dir++)
        {
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];

            if (nx < 0 || ny < 0 || nx >= R || ny >= C)
                continue;
            if (fire[nx][ny] >= 0 | grid[nx][ny] == '#')
                continue;
            Q2.push({nx, ny});
            fire[nx][ny] = fire[cur.X][cur.Y] + 1;
        }
    }

    // 미로 탈출 가능 ? - 빠른 탈출시간 (거리)
    while (!Q1.empty())
    {
        auto cur = Q1.front();
        Q1.pop();
        for (int dir = 0; dir < 4; dir++)
        {
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];
            // 지훈 - 가장자리에서 탈출이 가능하다.
            if (nx < 0 || ny < 0 || nx >= R || ny >= C)
            {
                cout << dist[cur.X][cur.Y] + 1;
                return 0;
            }
            // cout << "Test1\n";
            // dist 전개 조건 - 불이 있거나 벽이면 불가능
            if (dist[nx][ny] >= 0 || grid[nx][ny] == '#')
                continue;
            // 미방문 영역이지만, 불이 먼저 번지는 경우
            if (fire[nx][ny] != -1 && fire[nx][ny] <= dist[cur.X][cur.Y] + 1)
                continue;
            // cout << "Test2\n";
            Q1.push({nx, ny});
            dist[nx][ny] = dist[cur.X][cur.Y] + 1;
        }
    }

    // pr(fire); // test
    // pr(dist);
    // 불가능
    cout << "IMPOSSIBLE\n";

    return 0;
}