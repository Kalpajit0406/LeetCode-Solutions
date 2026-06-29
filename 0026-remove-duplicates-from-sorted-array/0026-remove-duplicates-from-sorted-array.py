class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: An empty array has 0 unique elements
        if not nums:
            return 0
            
        # Pointer to place the next unique element
        insert_index = 1
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is unique compared to the previous one
            if nums[i] != nums[i - 1]:
                nums[insert_index] = nums[i]
                insert_index += 1
                
        # insert_index represents the count of unique elements
        return insert_index