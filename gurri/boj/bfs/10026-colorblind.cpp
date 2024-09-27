// 교훈 : 문제를 잘 읽자
#include <bits/stdc++.h>
#define X first
#define Y second
using namespace std;
const int MX = 101;
int board1[MX][MX], vis[MX][MX], board2[MX][MX];
int N;

int bfs(int (&board)[MX][MX])
{
    int cnt = 0;
    queue<pair<int, int>> Q1;

    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, -1, 0, 1};

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            vis[i][j] = 0;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (!vis[i][j])
            {
                Q1.push({i, j});
                vis[i][j] = 1;
                cnt++;
            }

            while (!Q1.empty())
            {
                auto cur1 = Q1.front();
                Q1.pop();

                for (int i = 0; i < 4; i++)
                {
                    int nx1 = cur1.X + dx[i];
                    int ny1 = cur1.Y + dy[i];

                    if (nx1 < 0 || ny1 < 0 || nx1 >= N || ny1 >= N)
                        continue;
                    if (!vis[nx1][ny1] && board[nx1][ny1] == board[cur1.X][cur1.Y])
                    {
                        Q1.push({nx1, ny1});
                        vis[nx1][ny1] = 1;
                    }
                }
            }
        }
    }

    return cnt;
}

int main(void)
{

    // 10026 적록색약
    cin >> N;
    // 적록색약 아닐때, 적록색약일 때 보이는 구역을 출력하시오.
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            char c;
            cin >> c;
            if (c == 'G')
            {
                board1[i][j] = 1;
                board2[i][j] = 3;
            }
            if (c == 'R')
            {
                board1[i][j] = 1;
                board2[i][j] = 1;
            }
            if (c == 'B')
            {
                board1[i][j] = 2;
                board2[i][j] = 2;
            }
        }
    }
    int cnt1 = bfs(board1);
    int cnt2 = bfs(board2);

    cout << cnt2 << " " << cnt1 << '\n';

    return 0;
}