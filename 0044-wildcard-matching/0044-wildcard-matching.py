class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr, p_ptr = 0, 0
        s_star, p_star = -1, -1
        
        while s_ptr < len(s):
            # Case 1: Characters match or pattern has a '?' single character wildcard
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
                
            # Case 2: Pattern has a '*' sequence wildcard
            elif p_ptr < len(p) and p[p_ptr] == '*':
                p_star = p_ptr
                s_star = s_ptr
                p_ptr += 1  # Advance pattern pointer, assuming '*' matches 0 characters first
                
            # Case 3: Mismatch occurs, but we have a previous '*' to fallback on
            elif p_star != -1:
                p_ptr = p_star + 1  # Reset pattern pointer to right after the '*'
                s_star += 1         # Advance the fallback position to consume one character from s
                s_ptr = s_star      # Move string pointer to the updated fallback position
                
            # Case 4: Mismatch and no '*' wildcard available to salvage it
            else:
                return False
            
        # Check if any remaining characters in the pattern are only '*'
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            
        # If we successfully parsed the entire pattern, it's a valid match
        return p_ptr == len(p)