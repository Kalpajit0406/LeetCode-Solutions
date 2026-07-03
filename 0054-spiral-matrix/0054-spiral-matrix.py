from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
            
        # Initialize the boundary pointers
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        
        result = []
        
        while left <= right and top <= bottom:
            # 1. Traverse Right (along the top boundary)
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1 # Move the top boundary down
            
            # 2. Traverse Down (along the right boundary)
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1 # Move the right boundary left
            
            # 3. Traverse Left (along the bottom boundary)
            # We must verify top <= bottom because 'top' was recently incremented
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1 # Move the bottom boundary up
                
            # 4. Traverse Up (along the left boundary)
            # We must verify left <= right because 'right' was recently decremented
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1 # Move the left boundary right
                
        return result