class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        # component_id[i] will store the ID of the connected component for node i
        component_id = [0] * n
        curr_id = 0
        
        # Group nodes into contiguous connected components
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                curr_id += 1
            component_id[i] = curr_id
            
        # For each query, check if both nodes belong to the same component
        ans = []
        for u, v in queries:
            ans.append(component_id[u] == component_id[v])
            
        return ans