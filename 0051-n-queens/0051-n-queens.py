from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Sets to keep track of occupied paths
        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)
        
        res = []
        # Initialize an empty board filled with '.'
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r):
            # Base Case: If we've successfully placed queens in all rows
            if r == n:
                # Copy the current board state into a list of strings
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # Try placing a queen in each column of the current row `r`
            for c in range(n):
                # Check if the cell is under attack
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # Place the queen (Choose)
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                
                # Move to the next row (Explore)
                backtrack(r + 1)
                
                # Remove the queen (Unchoose / Backtrack)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
                
        # Start backtracking from the first row (row 0)
        backtrack(0)
        return res