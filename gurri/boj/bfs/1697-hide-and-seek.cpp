#include <bits/stdc++.h>
using namespace std;

// const int MX = 100002;
int dist[100002];
int n, k;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> k;
    // // 초기화
    fill(dist, dist + 100001, -1);
    dist[n] = 0;
    queue<int> Q;
    Q.push(n);

    // // while (dist[k] == -1)
    // // {
    while (dist[k] == -1)
    {
        //     int cur = Q.front();
        //     Q.pop();

        int cur = Q.front();
        Q.pop();
        for (int nxt : {cur - 1, cur + 1, 2 * cur})
        { // range-based for 문법
            if (nxt < 0 || nxt > 100000)
                continue;
            if (dist[nxt] != -1)
                continue;
            dist[nxt] = dist[cur] + 1;
            Q.push(nxt);
        }
    }
    cout << dist[k];
    return 0;
}
