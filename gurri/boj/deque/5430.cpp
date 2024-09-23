#include <bits/stdc++.h>
using namespace std;

void parse(string &tmp, deque<int> &dq)
{
    int cur = 0;
    for (int i = 1; i + 1 < tmp.size(); i++)
    {
        if (tmp[i] == ',')
        {
            dq.push_back(cur);
            cur = 0;
        }
        else
        {
            cur = 10 * cur + (tmp[i] - '0');
        }
    }
    if (cur != 0)
        dq.push_back(cur);
}

void print_result(deque<int> &dq)
{
    cout << '[';
    for (int i = 0; i < dq.size(); i++)
    {
        cout << dq[i];
        if (i + 1 != dq.size())
            cout << ',';
    }
    cout << "]\n";
}

int t;
int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> t;
    while (t--)
    {
        deque<int> dq;
        int rev = 0;
        int n;
        bool isWrong = false;
        string query, tmp;
        cin >> query;
        cin >> n;
        cin >> tmp;
        // parse to deque
        parse(tmp, dq);

        for (char c : query)
        {
            if (c == 'R')
                rev = 1 - rev;
            else
            {
                if (dq.empty())
                {
                    isWrong = true;
                    break;
                }
                if (!rev)
                    dq.pop_front();
                else
                    dq.pop_back();
            }
        }
        if (isWrong)
            cout << "error\n";
        else
        {
            // reverse 가능하다.
            if (rev)
                reverse(dq.begin(), dq.end());
            print_result(dq);
        }
    }

    return 0;
}