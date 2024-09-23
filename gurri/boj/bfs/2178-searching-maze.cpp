#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

const int MX = 102;
int board[MX][MX], vis[MX][MX], dist[MX][MX];

queue<pair<int, int>> Q;

int minArea;

int N, M;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0, 1};

void prboard()
{
    // Print Test
    for (int x = 0; x < N; x++)
    {
        for (int y = 0; y < M; y++)
            cout << board[x][y] << ' ';
        cout << '\n';
    }
}

void bfs(pair<int, int> start)
{
    Q.push(start);

    while (!Q.empty())
    {
        pair<int, int> cur = Q.front();
        Q.pop();
        minArea++;
        if (cur.X == N - 1 && cur.Y == M - 1)
            break;

        // cout << cur.X << " " << cur.Y << '\n';

        for (int dir = 0; dir < 4; dir++)
        {
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];

            if (nx < 0 || ny < 0 || nx >= N || ny >= M)
                continue;
            if (vis[nx][ny] || board[nx][ny] != 1)
                continue;
            vis[nx][ny] = 1;
            dist[nx][ny] = dist[cur.X][cur.Y] + 1;
            Q.push({nx, ny});
        }
    }
}

int main(void)
{

    cin >> N >> M;

    // 이거 어떻게 예외처리할까 ?
    string s;
    getline(cin, s);

    for (int i = 0; i < N; i++)
    {
        string s;
        getline(cin, s);

        for (int j = 0; j < M; j++)
        {
            board[i][j] = s[j] - '0';
        }
    }
    // prboard();
    vis[0][0] = 1;
    dist[0][0] = 1;
    bfs({0, 0});

    // cout << minArea << '\n';
    cout << dist[N - 1][M - 1] << '\n';
}
