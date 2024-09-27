#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

const int MX = 1001;
// 불부터 전개 후 사람을 전개
int dist1[MX][MX], dist2[MX][MX], board[MX][MX];

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

string s[MX];

int main(void)
{
    int T;
    cin >> T;

    while (T--)
    {
        int w, h;
        cin >> w >> h;
        int endx = -1, endy = -1;
        for (int i = 0; i < h; i++)
        {
            fill(dist1[i], dist1[i] + w, -1);
            fill(dist2[i], dist2[i] + w, -1);
        }
        queue<pair<int, int>> Q1, Q2;

        for (int i = 0; i < h; i++)
        {
            cin >> s[i];
            for (int j = 0; j < w; j++)
            {
                // 벽
                // if (s[i][j] == '#')
                // {
                //     dist1[i][j] = 0;
                //     dist2[i][j] = 0;
                // }
                if (s[i][j] == '@')
                {
                    dist2[i][j] = 0;
                    Q2.push({i, j});
                }
                if (s[i][j] == '*')
                {
                    dist1[i][j] = 0;
                    Q1.push({i, j});
                }
            }
        }

        while (!Q1.empty())
        {
            auto cur = Q1.front();
            Q1.pop();

            for (int dir = 0; dir < 4; dir++)
            {
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];
                if (nx < 0 || ny < 0 || nx >= h || ny >= w)
                    continue;
                if (dist1[nx][ny] >= 0 || s[nx][ny] == '#')
                    continue;

                dist1[nx][ny] = dist1[cur.X][cur.Y] + 1;
                Q1.push({nx, ny});
            }
        }
        bool isFinish = false;
        while (!Q2.empty())
        {
            auto cur = Q2.front();
            Q2.pop();

            for (int dir = 0; dir < 4; dir++)
            {
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];
                // 탈출 검사
                if ((nx < 0 || ny < 0 || nx >= h || ny >= w) && !isFinish)
                {
                    isFinish = true;
                    endx = cur.X;
                    endy = cur.Y;
                    // cout << endx << endy;
                    break;
                }
                if (dist2[nx][ny] >= 0 || s[nx][ny] == '#')
                    continue;
                // 불이 먼저 간다면 안됨
                if (dist1[nx][ny] != -1 && dist2[cur.X][cur.Y] + 1 >= dist1[nx][ny])
                    continue;
                dist2[nx][ny] = dist2[cur.X][cur.Y] + 1;
                Q2.push({nx, ny});
            }
        }

        if (endx != -1 && endy != -1)
            cout << dist2[endx][endy] + 1 << '\n';
        else
            cout << "IMPOSSIBLE\n";
    }

    return 0;
}