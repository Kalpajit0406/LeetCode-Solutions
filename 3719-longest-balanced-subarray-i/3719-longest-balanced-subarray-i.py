class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        max_len = 0
        
        # Try every possible starting position for the subarray
        for i in range(n):
            distinct_evens = set()
            distinct_odds = set()
            
            # Expand the subarray to the right
            for j in range(i, n):
                val = nums[j]
                
                # Categorize the current number
                if val % 2 == 0:
                    distinct_evens.add(val)
                else:
                    distinct_odds.add(val)
                
                # If the count of distinct evens equals distinct odds, check length
                if len(distinct_evens) == len(distinct_odds):
                    max_len = max(max_len, j - i + 1)
                    
        return max_len