#include <bits/stdc++.h>
using namespace std;

deque<int> Deque;
int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    int x;
    while (N-- > 0)
    {
        string s;
        cin >> s;
        if (s == "push_front")
        {
            cin >> x;
            Deque.push_front(x);
        }
        else if (s == "push_back")
        {
            cin >> x;
            Deque.push_back(x);
        }
        else if (s == "pop_front")
        {
            if (!Deque.empty())
            {
                cout << Deque.front() << '\n';
                Deque.pop_front();
            }
            else
                cout << "-1\n";
        }
        else if (s == "pop_back")
        {
            if (!Deque.empty())
            {
                cout << Deque.back() << '\n';
                Deque.pop_back();
            }
            else
                cout << "-1\n";
        }
        else if (s == "size")
        {
            cout << Deque.size() << '\n';
        }
        else if (s == "front")
        {
            if (!Deque.empty())
            {
                cout << Deque.front() << '\n';
            }
            else
                cout << "-1\n";
        }
        else if (s == "back")
        {
            if (!Deque.empty())
            {
                cout << Deque.back() << '\n';
            }
            else
                cout << "-1\n";
        }
        else
        {
            cout << (Deque.empty()) << '\n';
        }
    }

    return 0;
}