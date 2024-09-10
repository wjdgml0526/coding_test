from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for _ in range(len(board)):
        #     print(*board[_])

        # row
        for row in range(9):
            cnt = defaultdict(int)

            for col in range(9):
                if board[row][col] != '.':
                    cnt[board[row][col]] += 1
            
            for k, v in cnt.items():
                if v > 1 : 
                    return False

        # col
        for col in range(9):
            cnt = defaultdict(int)

            for row in range(9):
                if board[row][col] != '.':
                    cnt[board[row][col]] += 1
            
            for k, v in cnt.items():
                if v > 1 : 
                    return False

        # box
        for i in range(3):
            for j in range(3):

                cnt = defaultdict(int)
                # (3*i, 3*j)에서 3, 3 으로 

                for row in range(3):
                    for col in range(3):
                        if board[3*i+row][3*j+col] != '.':
                            cnt[board[3*i+row][3*j+col]] += 1

                print(cnt)
                for k, v in cnt.items():
                    if v > 1 : 
                        return False
                    
        return True 