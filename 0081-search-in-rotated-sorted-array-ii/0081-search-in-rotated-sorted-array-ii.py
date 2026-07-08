class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
                
            # Edge case: handling duplicate boundaries where we can't determine the sorted half
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
                
            # Case 1: Left half is properly sorted
            if nums[left] <= nums[mid]:
                # Check if the target falls within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # Case 2: Right half is properly sorted
            else:
                # Check if the target falls within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False