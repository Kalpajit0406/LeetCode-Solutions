class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(r: int, c: int, index: int) -> bool:
            # Base Case: all characters in the word have been matched
            if index == len(word):
                return True
                
            # Boundary conditions and character mismatch check
            if (r < 0 or r >= m or 
                c < 0 or c >= n or 
                board[r][c] != word[index]):
                return False
            
            # Temporarily mark the cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all 4 adjacent directions
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            # Backtrack: restore the cell's original value
            board[r][c] = temp
            
            return found

        # Try to start DFS from every cell in the grid
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                        
        return False