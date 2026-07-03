from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Define the initial boundaries
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        
        # Start filling from 1 up to n^2
        num = 1
        
        while left <= right and top <= bottom:
            # 1. Traverse Right (along the top boundary)
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1  # Move top boundary down
            
            # 2. Traverse Down (along the right boundary)
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1  # Move right boundary left
            
            # 3. Traverse Left (along the bottom boundary)
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1  # Move bottom boundary up
            
            # 4. Traverse Up (along the left boundary)
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1  # Move left boundary right
            
        return matrix