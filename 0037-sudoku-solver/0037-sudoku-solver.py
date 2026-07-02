class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        
        # Step 1: Initialize our sets with the numbers already on the board
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    # Convert 2D box coordinate (r//3, c//3) to a 1D index from 0 to 8
                    box_idx = (r // 3) * 3 + (c // 3)
                    squares[box_idx].add(val)
        
        # Step 2: Define the recursive backtracking function
        def backtrack(r, c) -> bool:
            # If we reach the end of a row, move to the next row
            if c == 9:
                r += 1
                c = 0
            # If we successfully filled the entire board, we are done
            if r == 9:
                return True
            
            # If the current cell is already filled, skip to the next cell
            if board[r][c] != '.':
                return backtrack(r, c + 1)
            
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Try placing digits 1-9
            for digit in map(str, range(1, 10)):
                if digit not in rows[r] and digit not in cols[c] and digit not in squares[box_idx]:
                    # Make a choice
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    squares[box_idx].add(digit)
                    
                    # Recurse to see if this choice leads to a solution
                    if backtrack(r, c + 1):
                        return True
                    
                    # Backtrack if it didn't work out
                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    squares[box_idx].remove(digit)
            
            return False

        backtrack(0, 0)