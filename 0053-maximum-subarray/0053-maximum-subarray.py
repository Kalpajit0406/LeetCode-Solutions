from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize with the first element
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Iterate from the second element onwards
        for i in range(1, len(nums)):
            # Either extend the existing subarray or start a new one
            current_sum = max(nums[i], current_sum + nums[i])
            # Update the absolute maximum found so far
            max_sum = max(max_sum, current_sum)
            
        return max_sum