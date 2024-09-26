#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

const int MX = 101;
int board[MX][MX], vis[MX][MX];

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int M, N, K;
vector<int> V;

void fillArea(int K)
{
    while (K--)
    {
        int y1, x1, y2, x2;
        cin >> y1 >> x1 >> y2 >> x2;
        for (int x = x1; x < x2; x++)
        {
            for (int y = y1; y < y2; y++)
            {
                board[x][y] = 1;
            }
        }
    }
    // check square
    // for (int i = 0; i < M; i++)
    // {
    //     for (int j = 0; j < N; j++)
    //     {
    //         cout << board[i][j] << " ";
    //     }
    //     cout << '\n';
    // }
}

int bfs(int x, int y)
{
    int cnt = 1;
    queue<pair<int, int>> Q;

    Q.push({x, y});
    vis[x][y] = 1;

    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();

        for (int dir = 0; dir < 4; dir++)
        {
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];

            if (nx < 0 || ny < 0 || nx >= M || ny >= N)
                continue;
            if (vis[nx][ny] == 1 || board[nx][ny] == 1)
                continue;
            Q.push({nx, ny});
            vis[nx][ny] = 1;
            cnt++;
        }
    }

    return cnt;
}

int main(void)
{

    cin >> M >> N >> K;

    fillArea(K);

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (vis[i][j] == 0 && board[i][j] == 0)
            {
                int cnt = bfs(i, j);
                V.push_back(cnt);
            }
        }
    }
    sort(V.begin(), V.end());
    cout << V.size() << '\n';
    for (auto v : V)
    {
        cout << v << " ";
    }

    return 0;
}