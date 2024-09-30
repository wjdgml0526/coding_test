#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

int board[8][8], check[8][8];
int N, M;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

vector<pair<int, int>> cctv; // cctv 좌표 저장

bool OOB(int a, int b){
    return a < 0 || a >= N || b < 0 || b>=M;
}

int minArea;

void upd(int x, int y, int dir){
    dir %= 4; // 방향 보정
    while (1){
        x += dx[dir];
        y += dy[dir];
        if (OOB(x, y) || check[x][y] == 6) return;
        if (check[x][y] != 0)
        continue;
        check[x][y] = 7;
    }
}

int main(void){
    
    cin >> N >> M;
    int mn = 0;
    for (int i=0;i<N;i++)
    for (int j=0;j<M;j++) 
    {
        cin >> board[i][j];
        if (board[i][j]>=1 && board[i][j] <6) cctv.push_back({i, j});
        if (board[i][j] == 0) mn++;
    }
    
    // 사각지대를 최소화
    // 1 ~ 5 는 CCTV
    for (int tmp = 0; tmp < (1 <<(2*cctv.size())); tmp++){// tmp를 4진법으로 뒀을 때 각 자리수를 cctv의 방향으로
        for (int i=0; i<N;i++){
            for (int j=0;j<M;j++){
                check[i][j] = board[i][j];
            }
        }

        int brute = tmp;
        
        for (int i=0; i< cctv.size(); i++){
            // 4진법 방향 적용
            int dir = brute % 4; // 해당 방향
            brute /= 4; // 자리수 변환

            int x = cctv[i].X;
            int y = cctv[i].Y; // tie(x, y) = cctv[i];로 쓰면 한줄로 가능 ? 

            if (board[x][y] == 1){
                upd(x, y, dir);
            }
            else if (board[x][y] == 2){
                upd(x, y, dir);
                upd(x, y, dir+2);
            }
            else if (board[x][y] == 3){
                upd(x, y, dir);
                upd(x, y, dir+1);
            }
            else if (board[x][y] == 4){
                upd(x, y, dir);
                upd(x, y, dir+1);
                upd(x, y, dir+2);
            }
            else if (board[x][y] == 5){
                upd(x, y, dir);
                upd(x, y, dir+1);
                upd(x, y, dir+2);
                upd(x, y, dir+3);
            }
        }
        int val = 0;
        for (int i=0; i<N; i++)
        for(int j=0; j<M;j++)
        val += (check[i][j] == 0);
        mn = min(mn, val);
    } 

    cout << mn << '\n';
}