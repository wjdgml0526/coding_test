#include <bits/stdc++.h>
using namespace std;

const int MX = 2500;
int board[MX][MX], cnt[3];

bool check(int x, int y, int N)
{
    for (int i = x; i < x + N; i++)
        for (int j = y; j < y + N; j++)
            if (board[x][y] != board[i][j])
                return false;
    return true;
}

void solve(int x, int y, int z)
{

    // base
    if (check(x, y, z))
    {
        cnt[board[x][y] + 1] += 1;
        return;
    }

    // recursive
    int n = z / 3;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            solve(x + i * n, y + j * n, n);
        }
    }
}

int main(void)
{
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> board[i][j];
        }
    }

    solve(0, 0, N);

    for (int i = 0; i < 3; i++)
        cout << cnt[i] << '\n';
}
