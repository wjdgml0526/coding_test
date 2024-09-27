#include <bits/stdc++.h>
using namespace std;
// 하노이의 탑

void func(int n, int a, int b)
{
    // n째 원판을 a -> b로 옮김

    // base condition
    if (n == 1)
    {
        cout << a << ' ' << b << '\n';
        return;
    }
    // 선행조건
    // 1 - n-1까지를 a -> 6-a-b로 옮겨야 함
    func(n - 1, a, 6 - a - b);
    // n 원판을 a -> b로 옮김
    cout << a << ' ' << b << '\n';
    // n-1 까지 원판을 6-a-b -> b로 옮겨야 함
    func(n - 1, 6 - a - b, b);
}

int main(void)
{
    int K;
    cin >> K;

    cout << (1 << K) - 1 << '\n';
    func(K, 1, 3);
}