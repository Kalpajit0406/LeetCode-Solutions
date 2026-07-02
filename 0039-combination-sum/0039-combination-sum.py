class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, current_combination, current_sum):
            # Base Case: If the current sum matches the target, we found a valid combination
            if current_sum == target:
                res.append(list(current_combination))
                return
            
            # Base Case: If sum exceeds target or we run out of candidates, stop searching
            if current_sum > target or i >= len(candidates):
                return
            
            # Decision 1: Include candidates[i]
            current_combination.append(candidates[i])
            dfs(i, current_combination, current_sum + candidates[i])
            
            # Backtrack: Clean up the choice before trying the next path
            current_combination.pop()
            
            # Decision 2: Exclude candidates[i] and move to the next index
            dfs(i + 1, current_combination, current_sum)
            
        dfs(0, [], 0)
        return res