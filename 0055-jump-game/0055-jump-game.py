from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        target = len(nums) - 1
        
        for i, jump in enumerate(nums):
            # If the current index is unreachable, we can't move forward
            if i > max_reachable:
                return False
            
            # Update the furthest index we can reach
            max_reachable = max(max_reachable, i + jump)
            
            # Early exit: if we can already reach or pass the last index
            if max_reachable >= target:
                return True
                
        return max_reachable >= target