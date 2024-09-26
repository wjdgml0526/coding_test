#include <bits/stdc++.h>
using namespace std;

// Night의 이동

#define X first
#define Y second

const int MX = 301;
int vis[MX][MX];
int T;
int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int dx[8] = {2, 1, -1, -2, -2, -1, 1, 2};
    int dy[8] = {1, 2, 2, 1, -1, -2, -2, -1};

    cin >> T;
    while (T--)
    {
        int l;
        pair<int, int> start, end;

        // 최소 이동 가능한 횟수 ?
        int cnt = 0;
        queue<pair<int, int>> Q;
        cin >> l >> start.X >> start.Y >> end.X >> end.Y;

        // 초기화
        for (int i = 0; i < l; i++)
            fill(vis[i], vis[i] + l, -1);

        Q.push(start);
        vis[start.X][start.Y] = 0;

        while (!Q.empty())
        {
            auto cur = Q.front();
            Q.pop();
            if (cur == end)
                break;
            for (int dir = 0; dir < 8; dir++)
            {
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];

                if (nx < 0 || ny < 0 || nx >= l || ny >= l)
                    continue;
                if (vis[nx][ny] >= 0)
                    continue;
                // cout << nx << ' ' << ny;
                Q.push({nx, ny});
                vis[nx][ny] = vis[cur.X][cur.Y] + 1;
            }
        }

        cout << vis[end.X][end.Y] << '\n';
    }
    return 0;
}