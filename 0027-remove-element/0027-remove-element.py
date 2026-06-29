class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer to place the next element that is not equal to val
        insert_index = 0
        
        # Traverse the array
        for i in range(len(nums)):
            # If the current element is not the value we want to remove
            if nums[i] != val:
                nums[insert_index] = nums[i]
                insert_index += 1
                
        # insert_index now represents the number of elements not equal to val
        return insert_index