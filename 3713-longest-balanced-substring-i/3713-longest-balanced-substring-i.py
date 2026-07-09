class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        # Try every possible starting position of the substring
        for i in range(n):
            # Frequency map for characters in the current substring
            char_counts = {}
            
            # Expand the substring to the right
            for j in range(i, n):
                char = s[j]
                char_counts[char] = char_counts.get(char, 0) + 1
                
                # Check if all distinct characters appear the same number of times
                counts_set = set(char_counts.values())
                
                # If there's only 1 unique frequency value, the substring is balanced
                if len(counts_set) == 1:
                    max_len = max(max_len, j - i + 1)
                    
        return max_len