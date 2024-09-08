class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 입력된 리스트에서 중복된 숫자가 있으면 False 반환하는 함수
        def check_duplicate(nums):
            new_nums = list(filter(lambda x: x != '.', nums))
            return len(set(new_nums)) == len(new_nums)
        
        for i in range(len(board)):
            # row에서 중복된 숫자가 있는지 확인
            if not check_duplicate(board[i]):
                return False
            # col에서 중복된 숫자가 있는지 확인
            if not check_duplicate(list(zip(*board))[i]):
                return False
            # sub_board에서 중복된 숫자가 있는지 확인
            strt_row, strt_col = (i // 3) * 3, (i % 3) * 3
            sub_board = [row[strt_col: strt_col + 3] for row in board[strt_row: strt_row + 3]]
            sub_board = sum(sub_board, [])
            if not check_duplicate(sub_board):
                return False
        else:
            return True