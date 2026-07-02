class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize result array to hold the max possible digits
        res = [0] * (len(num1) + len(num2))
        
        # Loop backwards through both strings
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Multiply the single digits (converting character to int via ASCII offset)
                digit_prod = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                # Positions in the result array where this product contributes
                p1 = i + j
                p2 = i + j + 1
                
                # Sum the current product with any existing values at the target position
                total_sum = digit_prod + res[p2]
                
                # Update carry and remainder
                res[p1] += total_sum // 10
                res[p2] = total_sum % 10
                
        # Skip leading zero if it exists in the highest position
        start_idx = 1 if res[0] == 0 else 0
        
        # Convert integers back to string characters and join them
        return "".join(map(str, res[start_idx:]))