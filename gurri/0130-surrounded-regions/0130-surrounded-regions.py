class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        q = []
        
        r = len(board)
        if r == 0: return
        c = len(board[0])
        if c == 0: return
        
        # First append all the corner Os and then do bfs on these values to get the 
        # neighbor Os. All Os which are connected to any corner O need to be remain 
        # as O. So replace them with T and then revert it back to O.
        for i in range(r):
            for j in range(c):
                if (i == 0 or j == 0 or i == r - 1 or j == c - 1) and board[i][j] == "O":
                    q.append((i,j))


        while q:
            i, j = q.pop(0)
            board[i][j] = "T"
            for x,y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                x_n = i + x
                y_n = j + y
                
                if x_n >= 0 and x_n < r and y_n >= 0 and y_n < c and board[x_n][y_n] == "O":
                    q.append((x_n, y_n))
                    
        
        for i in range(r):
            for j in range(c):   
                if board[i][j] == "O": # Os are the indexes which are covered by Xs
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"