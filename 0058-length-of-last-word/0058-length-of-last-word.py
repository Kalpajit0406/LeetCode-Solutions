class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split() without arguments automatically strips whitespace and handles gaps
        words = s.split()
        
        # Return the length of the last word in the list
        return len(words[-1])