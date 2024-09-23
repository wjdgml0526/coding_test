#include <bits/stdc++.h>
using namespace std;

deque<int> DQ;
int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, M;
    cin >> N >> M;

    for (int i = 1; i <= N; i++)
        DQ.push_back(i);
    int ans = 0;

    while (M--)
    {
        int t;
        cin >> t;
        // 위치 확인
        int idx = find(DQ.begin(), DQ.end(), t) - DQ.begin();
        while (DQ.front() != t)
        {
            if (idx < DQ.size() - idx)
            {
                DQ.push_back(DQ.front());
                DQ.pop_front();
            }
            else
            {
                DQ.push_front(DQ.back());
                DQ.pop_back();
            }
            ans++;
        }
        DQ.pop_front();
    }
    cout << ans;

    return 0;
}