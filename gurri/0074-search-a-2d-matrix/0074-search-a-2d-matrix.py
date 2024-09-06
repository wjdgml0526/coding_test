class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # inspect whether the target is in ?

        nums_firstcol = [matrix[i][0] for i in range(len(matrix))]

        # 1. find row_index - not exactly matched 
        l, r = 0, len(matrix) - 1

        while l <= r : 
            mid = (l+r)//2
            
            if nums_firstcol[mid] == target : 
                return True

            # 위
            if nums_firstcol[mid] < target: 
                l = mid + 1
            # 아래
            else : 
                r = mid - 1

        # r_row에 있음

        # 2. find col_index - must match
        nums_row = matrix[r]

        l, r = 0, len(nums_row) - 1

        while l <= r : 
            mid = (l+r)//2
            
            if nums_row[mid] == target : 
                return True

            # 위
            if nums_row[mid] < target: 
                l = mid + 1
            # 아래
            else : 
                r = mid - 1
        return False