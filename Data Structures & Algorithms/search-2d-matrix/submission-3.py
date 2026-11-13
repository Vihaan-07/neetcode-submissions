class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find which row to search
        l = 0 
        r = len(matrix) -1
        col = len(matrix[0]) - 1
        target_row = -1
        while l <= r:
            m = (l + r) // 2

            if matrix[m][col] == target: 
                return True
            
            if matrix[m][col] > target and (matrix[m-1][col] < target or m == 0):
                target_row = m
                break
            
            if matrix[m][col] > target:
                r = m-1
            else:
                l = m+1
        

        if target_row == -1:
            return False
        
        l = 0
        r = len(matrix[target_row]) -1
        # print(f"l: {l} r: {r}")
        while l <= r:
            m = (l+r) // 2
            # print(f"Element to check: {matrix[target_row][m]}")
            if matrix[target_row][m] == target:
                return True
            
            elif matrix[target_row][m] > target:
                r = m-1
            
            else:
                l = m+1
        
        return False

            

        