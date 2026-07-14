class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        res = max_prod = min_prod = nums[0]
        
        for i in range(1, len(nums)):
            x = nums[i]
            # Store the temporary max because max_prod updates before min_prod calculation
            temp = max(x, max_prod * x, min_prod * x)
            min_prod = min(x, max_prod * x, min_prod * x)
            max_prod = temp
            
            res = max(res, max_prod)
            
        return res