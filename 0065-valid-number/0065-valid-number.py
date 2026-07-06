class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_e = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                
            elif char in ('+', '-'):
                # Signs can only appear at index 0 or right after an exponent 'e'/'E'
                if i > 0 and s[i - 1] not in ('e', 'E'):
                    return False
                    
            elif char in ('e', 'E'):
                # Exponent can't appear twice, and must follow at least one digit
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False  # Must be followed by a new integer
                
            elif char == '.':
                # Dot can't appear twice, and can't appear after an exponent
                if seen_dot or seen_e:
                    return False
                seen_dot = True
                
            else:
                # Any other character (like letters 'abc') is invalid
                return False
                
        # The string is only valid if it ends with a valid digit sequence
        return seen_digit