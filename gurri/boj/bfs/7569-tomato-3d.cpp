// tomato 3D
#include <bits/stdc++.h>
using namespace std;
// M x N x H의 상자. 익은 토마토에 인접한 토마토는 영향을 받아 익게 됨.
// 토마토가 전부 익는 데에 소요되는 최소 일수
#define X first
#define Y second
#define Z third

const int MX = 101;
int box[MX][MX][MX], dist[MX][MX][MX];
int M, N, H;
queue<tuple<int, int, int>> Q;

int main(void)
{
    cin >> M >> N >> H;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            fill(dist[i][j], dist[i][j] + H, -1);
        }
    }
    for (int k = 0; k < H; k++)
    {
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {

                cin >> box[i][j][k];
                // cout << i << j << k;
                // 익은 토마토라면
                if (box[i][j][k] == 1)
                {

                    dist[i][j][k] = 0;
                    Q.push({i, j, k});
                }

                if (box[i][j][k] == 0)
                {

                } // 익은 토마토라면
                if (box[i][j][k] == -1)
                {
                    dist[i][j][k] = 0;
                } // 익은 토마토라면
            }
        }
    }
    int dx[6] = {1, 0, -1, 0, 0, 0};
    int dy[6] = {0, 1, 0, -1, 0, 0};
    int dz[6] = {0, 0, 0, 0, 1, -1};

    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();

        for (int dir = 0; dir < 6; dir++)
        {
            int nx = get<0>(cur) + dx[dir];
            int ny = get<1>(cur) + dy[dir];
            int nz = get<2>(cur) + dz[dir];

            if (nx < 0 || ny < 0 || nz < 0 || nx >= N || ny >= M || nz >= H)
                continue;
            if (dist[nx][ny][nz] >= 0 || box[nx][ny][nz] == -1)
                continue;
            dist[nx][ny][nz] = dist[get<0>(cur)][get<1>(cur)][get<2>(cur)] + 1;
            Q.push({nx, ny, nz});
        }
    }
    int maxi = 0;
    // for (int k = 0; k < H; k++)
    // {
    //     for (int i = 0; i < N; i++)
    //     {
    //         for (int j = 0; j < M; j++)
    //         {

    //             cout << dist[i][j][k] << ' ';
    //         }
    //         cout << '\n';
    //     }
    // }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            for (int k = 0; k < H; k++)
            {
                if (dist[i][j][k] < 0)
                {
                    cout << -1 << '\n';
                    return 0;
                }
                maxi = max(dist[i][j][k], maxi);
            }
        }
    }

    cout << maxi << '\n';

    return 0;
}