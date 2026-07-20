from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings
        num_strs = [str(num) for num in nums]
        
        # Custom comparison function
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
                
        # Sort using the custom comparator
        num_strs.sort(key=cmp_to_key(compare))
        
        # Join the sorted strings
        result = "".join(num_strs)
        
        # Handle edge case where the largest number is "0" (e.g., [0, 0])
        return "0" if result[0] == "0" else result