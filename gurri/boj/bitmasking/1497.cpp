#include <bits/stdc++.h>
using namespace std;
int N, M;
long long state[10];

int bit_cnt(long long x)
{
    int ret = 0;
    // 비교해서 더하기
    for (int i = 0; i < max(N, M); i++)
    {
        ret += (x >> i) & 1;
    }
    return ret;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        string name, tmp;
        cin >> name >> tmp;
        for (int j = M - 1; j >= 0; j--)
        {
            state[i] = (state[i] << 1) | (tmp[j] == 'Y');
        }
    }

    pair<int, int> ans = {0, -1}; // (연주 할 수 있는 곡, 필요한 기타 수)
    for (int tmp = 0; tmp < (1 << N); tmp++)
    {
        long long comb = 0; // 조합한 결과
        for (int i = 0; i < N; i++)
        {
            if ((tmp & (1LL << i)) == 0)
                continue;
            comb |= state[i];
        }
        int song_num = bit_cnt(comb);
        int guitar_num = bit_cnt(tmp);

        if (ans.first < song_num) // 연주할 수 있는 곡이 더 많으면
            ans = {song_num, guitar_num};

        else if (ans.first == song_num && ans.second > guitar_num)
            ans = {song_num, guitar_num};
    }
    cout << ans.second << '\n';
}