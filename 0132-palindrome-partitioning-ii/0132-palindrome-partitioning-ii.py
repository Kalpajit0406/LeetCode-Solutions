class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # dp[i][j] will be True if s[i..j] is a palindrome
        dp = [[False] * n for _ in range(n)]
        
        # cuts[i] will store the minimum cuts needed for s[0..i]
        cuts = [0] * n
        
        for i in range(n):
            min_cuts = i  # Maximum cuts needed for s[0..i] is i
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if j == 0:
                        min_cuts = 0
                    else:
                        min_cuts = min(min_cuts, cuts[j - 1] + 1)
            cuts[i] = min_cuts
            
        return cuts[n - 1]