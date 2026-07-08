class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start: int, path: List[int]):
            # Every tracking state forms a valid subset
            res.append(list(path))
            
            for i in range(start, len(nums)):
                # Include the element
                path.append(nums[i])
                # Move onto the next elements
                backtrack(i + 1, path)
                # Exclude the element (backtrack)
                path.pop()
                
        backtrack(0, [])
        return res