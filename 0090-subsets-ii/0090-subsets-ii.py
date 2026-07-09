class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        # Sort the array so that duplicates are adjacent
        nums.sort()
        
        def backtrack(start: int, current_subset: list[int]):
            # Add a copy of the current subset to our results
            res.append(list(current_subset))
            
            for i in range(start, len(nums)):
                # If the current element is a duplicate of the previous element
                # AND we are not at the starting point of this decision level, skip it.
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Include nums[i] in the subset
                current_subset.append(nums[i])
                # Move to the next element
                backtrack(i + 1, current_subset)
                # Backtrack: remove nums[i] before the next iteration
                current_subset.pop()
                
        backtrack(0, [])
        return res