class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        current_permutation = []
        used = [False] * len(nums)
        
        # Sort the numbers to bring duplicates together
        nums.sort()
        
        def backtrack():
            # Base Case: If the current permutation contains all elements
            if len(current_permutation) == len(nums):
                res.append(list(current_permutation))
                return
            
            for i in range(len(nums)):
                # Skip if this element is already used in the current path
                if used[i]:
                    continue
                
                # Skip if this element is a duplicate of the previous element
                # AND the previous element was not used in this decision level
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                # Make a choice
                used[i] = True
                current_permutation.append(nums[i])
                
                # Recurse down the decision tree
                backtrack()
                
                # Backtrack: Clean up the state for the next branch
                current_permutation.pop()
                used[i] = False
                
        backtrack()
        return res