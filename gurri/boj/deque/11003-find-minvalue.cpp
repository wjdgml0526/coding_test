#include <bits/stdc++.h>
using namespace std;

deque<pair<int, int>> DQ;
int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, M;
    cin >> N >> M;

    for (int i = 0; i < N; ++i)
    {
        int num;
        cin >> num;

        while (!DQ.empty() && DQ.back().second >= num)
        {
            DQ.pop_back();
        }

        DQ.push_back({i, num});

        if (DQ.front().first <= i - M)
        {
            DQ.pop_front();
        }

        cout << DQ.front().second << " ";
    }

    return 0;
}