class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        
        def backtrack(current_permutation):
            # Base Case: If the current permutation is complete
            if len(current_permutation) == len(nums):
                res.append(list(current_permutation))
                return
            
            # Explore choices for the current position
            for num in nums:
                if num not in visited:
                    # Make a choice
                    visited.add(num)
                    current_permutation.append(num)
                    
                    # Recurse down the decision tree
                    backtrack(current_permutation)
                    
                    # Backtrack: Clean up the state for the next branch
                    current_permutation.pop()
                    visited.remove(num)
                    
        backtrack([])
        return res