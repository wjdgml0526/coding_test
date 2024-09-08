class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            start, end = 0, len(row) - 1
            
            while start <= end:
                mid = (start + end) // 2
                
                if row[mid] < target:
                    start = mid + 1
                    
                elif row[mid] > target:
                    end = mid -1
                    
                else:
                    return True
                    
        return False