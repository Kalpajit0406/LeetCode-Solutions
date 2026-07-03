import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of available numbers: [1, 2, 3, ..., n]
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Calculate factorials up to (n-1)!
        # factorials[i] will store i!
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i
            
        # Convert k to 0-indexed
        k -= 1
        
        result = []
        
        # Determine each digit from left to right
        for i in range(n - 1, -1, -1):
            # Current block size is i!
            block_size = factorials[i]
            
            # Find the index of the next number to use
            idx = k // block_size
            
            # Append the selected number to our result
            result.append(numbers[idx])
            # Remove it from the list of available numbers
            numbers.pop(idx)
            
            # Update k for the next iteration
            k %= block_size
            
        return "".join(result)