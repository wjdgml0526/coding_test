#include <bits/stdc++.h>
using namespace std;
int main(void)
{
    string s;
    cin >> s;
    int ans = 0;
    stack<char> S;
    int val = 1;

    for (int i = 0; i < s.size(); i++)
    {
        // cout << val << ' ' << ans << '\n';

        if (s[i] == '(')
        {
            S.push(s[i]);
            val *= 2;
        }

        else if (s[i] == '[')
        {
            S.push(s[i]);
            val *= 3;
        }
        else // Closing bracket
        {
            if (!S.empty()) // Stack isn't empty
            {
                if (S.top() == '(' && s[i] == ']' || S.top() == '[' && s[i] == ')')
                {
                    cout << 0;
                    return 0;
                }
                if (s[i] == ')' && S.top() == '(')
                {
                    if (s[i - 1] == '(')
                        ans += val;
                    val /= 2;
                    S.pop();
                }
                else if (s[i] == ']' && S.top() == '[')
                {
                    if (s[i - 1] == '[')
                        ans += val;
                    val /= 3;
                    S.pop();
                }
                else
                {
                    cout << 0;
                    return 0;
                }
            }
            else // empty
            {
                cout << 0;
                return 0;
            }
        }
    }

    if (!S.empty()) // Stack isn't empty
    {
        cout << 0;
        return 0;
    }
    cout << ans;

    return 0;
}