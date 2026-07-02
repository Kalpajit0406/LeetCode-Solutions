class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Sort candidates to easily handle duplicates and optimize pruning
        candidates.sort()
        
        def backtrack(i, current_combination, current_sum):
            # Base Case: If the current sum matches the target, we found a valid combination
            if current_sum == target:
                res.append(list(current_combination))
                return
            
            # Base Case: If sum exceeds target, stop searching (pruning)
            if current_sum > target:
                return
            
            for j in range(i, len(candidates)):
                # Skip duplicate elements at the same decision level
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                # Early optimization: If this element exceeds the target, 
                # all subsequent elements will too (since the array is sorted)
                if current_sum + candidates[j] > target:
                    break
                    
                # Make a choice
                current_combination.append(candidates[j])
                
                # Move to the next index (j + 1) because each element can only be used once
                backtrack(j + 1, current_combination, current_sum + candidates[j])
                
                # Backtrack: Clean up the choice
                current_combination.pop()
                
        backtrack(0, [], 0)
        return res