class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_col_zero = False
        
        # Step 1: Scan the matrix and use the first row/col as markers
        for i in range(m):
            # Check if the first column needs to be zeroed out later
            if matrix[i][0] == 0:
                first_col_zero = True
                
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # Step 2: Use the markers to set interior elements to zero
        # Iterate backwards or from index 1 to avoid overwriting headers prematurely
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # Step 3: See if the first row needs to be zeroed
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
                
        # Step 4: See if the first column needs to be zeroed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0