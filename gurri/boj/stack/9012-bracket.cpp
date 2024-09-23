#include <bits/stdc++.h>
using namespace std;

int T;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        string s;
        cin >> s;
        stack<char> S;
        for (auto ch : s)
        {
            if (ch == '(')
                S.push(ch);
            else // ch == ')'
            {
                if (S.empty())
                {
                    S.push(ch);
                    break;
                }

                else
                { // not empty
                    if (S.top() == '(')
                        S.pop(); // 짝이 맞음
                    else
                        break;
                }
            }
        }

        string out = (S.size()) ? "NO" : "YES";
        cout << out << "\n";
    }

    return 0;
}