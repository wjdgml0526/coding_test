
// 비트마스킹으로 다시
#include <bits/stdc++.h>
using namespace std;

int state;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int m;
    cin >> m;
    while (m--)
    {
        string com;
        int x;
        cin >> com;
        if (com == "add")
        {
            cin >> x;
            state |= (1 << (x-1));
        }
        else if (com == "remove")
        {
            cin >> x;
            // 연산 주의할 것
            state &= (~(1 << (x-1)));
        }
        else if (com == "check")
        {
            cin >> x;
            // 왜?
            cout << ((state >> (x-1) & 1)) << '\n';

        }
        else if (com == "toggle")
        {
            cin >> x;
            state ^= (1 << (x-1));
        }
        // 0xfffff : 4 * 5 0b1111 1111 1111 1111 1111
        else if (com == "all") state = 0xfffff; 
        else if (com == "empty") state=0;
    }
}

// #include <bits/stdc++.h>
// using namespace std;

// bool numSet[21];

// int main(void)
// {
//     ios::sync_with_stdio(0);
//     cin.tie(0);
//     fill(numSet, numSet + 21, false);
//     int M;
//     cin >> M;

//     while (M--)
//     {
//         int num;
//         string s;
//         cin >> s;
//         if (s == "add")
//         {
//             cin >> num;
//             numSet[num] = true;
//         }
//         else if (s == "remove")
//         {
//             cin >> num;
//             numSet[num] = false;
//         }
//         else if (s == "check")
//         {
//             cin >> num;
//             cout << (numSet[num] ? 1 : 0) << '\n';
//         }
//         else if (s == "toggle")
//         {
//             cin >> num;
//             if (numSet[num])
//                 numSet[num] = false;
//             else
//                 numSet[num] = true;
//         }
//         else if (s == "all")
//         {
//             for (int i = 1; i <= 20; i++)
//             {
//                 numSet[i] = true;
//             }
//         }
//         else
//         { // empty
//             for (int i = 1; i <= 20; i++)
//             {
//                 numSet[i] = false;
//             }
//         }
//     }

//     return 0;
// }