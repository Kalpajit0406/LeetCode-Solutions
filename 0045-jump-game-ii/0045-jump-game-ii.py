class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_jump_end = 0
        farthest = 0
        
        # We don't need to process the last element because once 
        # we can reach or pass it, we are done.
        for i in range(len(nums) - 1):
            # Update the farthest index we can reach from the current index
            farthest = max(farthest, i + nums[i])
            
            # If we have reached the end of the current jump's reach
            if i == current_jump_end:
                jumps += 1                  # Commit to a jump
                current_jump_end = farthest # Update our boundary for the next jump
                
                # Early exit optimization: if we can already reach the end, break
                if current_jump_end >= len(nums) - 1:
                    break
                    
        return jumps