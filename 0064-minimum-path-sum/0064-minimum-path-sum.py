class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Initialize a DP array representing a single row
        # Start with infinity so minimum calculations work smoothly
        dp = [float('inf')] * n
        dp[0] = 0  # Base case: no extra cost before entering the grid
        
        # Iterate through each cell in the grid row by row
        for r in range(m):
            for c in range(n):
                if c == 0:
                    # For the first column, we can only come from above
                    dp[c] = dp[c] + grid[r][c]
                else:
                    # Otherwise, take the min of coming from above (dp[c]) 
                    # or coming from the left (dp[c-1])
                    dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]
                    
        return dp[-1]