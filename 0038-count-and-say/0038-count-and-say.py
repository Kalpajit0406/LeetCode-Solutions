class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        current_str = "1"
        
        # Build the sequence iteratively up to n
        for _ in range(n - 1):
            next_str = []
            i = 0
            
            while i < len(current_str):
                count = 1
                # Count consecutive identical characters
                while i + 1 < len(current_str) and current_str[i] == current_str[i + 1]:
                    count += 1
                    i += 1
                
                # Append frequency followed by the character itself
                next_str.append(str(count))
                next_str.append(current_str[i])
                i += 1
                
            current_str = "".join(next_str)
            
        return current_str