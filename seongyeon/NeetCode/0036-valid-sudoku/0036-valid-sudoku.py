class Solution(object):
    def chk(self, arr):
        if len(arr) == 1:
            cnt = Counter([t for t in arr if t != '.']).values()
        else:
            cnt = Counter([t for tt in arr for t in tt if t != '.']).values()
        for c in cnt:
            if c > 1:
                return False

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for b in board:
            if self.chk(b) == False:
                return False
            else:
                continue

        for i in range(9):
            b = [b[i] for b in board]
            if self.chk(b) == False:
                return False
            else:
                continue
        
        for i in range(3):
            for j in range(3):
                b = [b[3*j:3*(j+1)] for b in board[3*i:3*(i+1)]]
                if self.chk(b) == False:
                    return False
                else:
                    continue
        return True
        