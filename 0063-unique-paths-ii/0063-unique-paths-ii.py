class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # Edge case: If the starting point or ending point has an obstacle, 
        # no paths are possible.
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
            
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # Initialize a DP array representing a single row
        dp = [0] * n
        dp[0] = 1 # Starting point has 1 way to begin
        
        # Iterate through every cell in the grid
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    # If there's an obstacle, 0 ways to reach or pass through it
                    dp[c] = 0
                elif c > 0:
                    # Otherwise, ways to reach current cell = 
                    # ways from top (already stored in dp[c]) + ways from left (dp[c-1])
                    dp[c] += dp[c - 1]
                    
        return dp[-1]