class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        # k points to the index where the next valid element will be inserted
        k = 2
        
        # Start checking from the 3rd element (index 2)
        for i in range(2, len(nums)):
            # If the current element is different from the element 2 positions back
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
                
        return k