class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        for i in range(numRows):
            # Create a row with 1s, where the row length matches the 0-indexed row number + 1
            row = [1] * (i + 1)
            
            # Update the middle elements of the row
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                
            triangle.append(row)
            
        return triangle