#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int cnt = 0;
    int tot = 0;
    string s;
    cin >> s;
    stack<char> S;

    for (int i = 0; i < s.size(); i++)
    {
        // 열린 괄호
        if (s[i] == '(')
            cnt++;
        else
        {
            cnt--;
            if (s[i - 1] == '(')
            {
                tot += cnt;
            }
            else
                tot++;
        }
    }
    cout << tot << '\n';
    return 0;
}