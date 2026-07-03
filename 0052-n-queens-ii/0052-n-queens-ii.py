class Solution:
    def totalNQueens(self, n: int) -> int:
        # Sets to track columns and diagonals under attack
        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)
        
        self.count = 0
        
        def backtrack(r):
            # Base Case: If we successfully placed a queen in all rows, increment count
            if r == n:
                self.count += 1
                return
            
            # Try placing a queen in each column of the current row `r`
            for c in range(n):
                # Check for conflicts
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # Choose: Place the queen
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                
                # Explore: Move to the next row
                backtrack(r + 1)
                
                # Unchoose: Remove the queen (Backtrack)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                
        # Start backtracking from the first row (row 0)
        backtrack(0)
        return self.count